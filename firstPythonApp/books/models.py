import email
from operator import mod
import profile
from re import T
from venv import create
from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    profile=models.URLField()
    created_at=models.DateField(auto_now_add=True)
    last_edit_at=models.DateField(auto_now=True)
    def __str__(self):
        return self.name

        
class Book(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    overview=models.CharField(max_length=400)
    image=models.URLField()
    upload_image = models.ImageField(upload_to='imgs/')
    author_id=models.ForeignKey(Author,on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    last_edit_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.title

