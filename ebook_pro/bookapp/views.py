from email.mime import message
import imp
from multiprocessing import context
from selectors import DefaultSelector
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from bookapp.forms import UserForm, LoginForm, BookForm
from django.contrib import messages


from django.views.generic import DetailView, ListView

from bookapp import models
from bookapp.models import Bookdetailsmodel

# 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test




# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required
def load_book_details(request):
    books_dict = {'key':Bookdetailsmodel.objects.all()}
    return render(request, 'books_list.html',books_dict)

@login_required
def user_logout(request):
    logout(request)
    return render(request,'index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()
        
    
    return render(request, 'register.html', {'user_form': user_form,'registered': registered})




def sign_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        #username = request.POST.get('username')
        #password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return load_book_details(request)
            else:
                print('User is not active look in ADMiN')

        else:
            print("Some one malicius tried to login")
            return HttpResponse("Invalid login credentials")
        
    else:
        login_form = LoginForm()
        return render(request,'signin.html',{'login_form':login_form})

@user_passes_test(lambda u: u.is_superuser)
def upload_book_details(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponse('Successfully Uploded!')
    else:
        form = BookForm()
        return render(request,'upload_data.html',{'form':form})


class BookDetailview(DetailView):
    context_object_name = 'book_detail'
    model = models.Bookdetailsmodel
    template_name = 'detailed_view.html'








            
