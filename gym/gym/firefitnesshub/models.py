from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Trainer(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='trainers_profile', blank=True)

class About(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to='about', blank=True)


class member(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)


class course(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='home', blank=True)


