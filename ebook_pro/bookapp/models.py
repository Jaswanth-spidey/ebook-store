from re import M
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Bookdetailsmodel(models.Model):
    profile_pic= models.ImageField(upload_to="images/")
    book_name = models.CharField(max_length=90, blank=False, null=False)
    book_price = models.FloatField(blank=False, null=False)
    book_description = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.book_name

