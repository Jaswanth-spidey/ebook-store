"""ebook_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import re
from django.contrib import admin
from django.urls import path,re_path
from bookapp import views


from django.conf import settings
from django.conf.urls.static import static
from bookapp.views import BookDetailview

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.index,name='index'),
    re_path(r'^sign_in/',views.sign_in,name='sign_in'),
    re_path(r'^register/',views.register,name='register'),
    re_path(r'^logout/',views.user_logout,name='logout'),
    re_path(r'^image_upload/',views.upload_book_details,name='image_upload'),
    re_path(r'^detail_view/(?P<pk>[\d]+)/$',views.login_required(BookDetailview.as_view()),name='detail_view'),
    re_path(r'book_list/',views.load_book_details,name='book_list'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

