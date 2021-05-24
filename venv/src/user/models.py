from django.db import models
from django.contrib.auth.models import User
from books.models import Book
# Create your models here.

class Reader(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE )
    username = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    
