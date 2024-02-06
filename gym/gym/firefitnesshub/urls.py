from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name="home"),
    path('about/', views.about, name='about'),
    path('trainers/',views.trainers_profile, name='trainer-profile'),
    path('membership', views.create_membership , name='membership'),
]