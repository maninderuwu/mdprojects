from django.shortcuts import render
from .models import advertise , Man, Woman

# Create your views here.
def home(request):
    ad=advertise.objects.all()
    men = Man.objects.all()
    women= Woman.objects.all()
    return render(request, 'home.html', {'ad':ad, 'men':men, 'women':women})


def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html')