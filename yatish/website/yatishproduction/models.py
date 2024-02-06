from django.db import models

# Create your models here.
class advertise(models.Model):
    name=models.CharField(max_length=25)

class Man(models.Model):
    man_name=models.CharField(max_length=100)
    man_description = models.TextField()
    man_images= models.ImageField(upload_to='home', blank=True, null=True)

    def __str__(self):
        return self.man_name

class Woman(models.Model):
    woman_name=models.CharField(max_length=100)
    woman_description = models.TextField()
    woman_images= models.ImageField(upload_to='home', blank=True, null=True)

    def __str__(self):
       return self.woman_name

    