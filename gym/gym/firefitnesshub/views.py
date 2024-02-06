from django.shortcuts import render, redirect
from .models import Trainer , About, course


# Create your views here.
def home(request):
    courses_object=course.objects.all()
    return render(request, 'home.html',{'courses_object':courses_object})


def trainers_profile(request):
    trainers= Trainer.objects.all()
    return render(request, 'trainer.html',{"trainers":trainers})



def about(request):
    about_objects = About.objects.all()
    return render(request, 'about.html', {'about_objects': about_objects})


def create_membership(request):
    return render(request, 'membership.html')
