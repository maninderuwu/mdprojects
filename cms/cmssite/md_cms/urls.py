from django.urls import path
from .views import add_article,article_details,edit_article,delete_article,article_list,signup,logout_user,home
from django.contrib.auth import views as auth_view

urlpatterns=[
    path('',home,name='home'),
    path('article/', article_list, name='article_list'),
    path('article/<int:pk>/', article_details, name='article_detail'),
    path('article/add/', add_article, name='add_article'),
    path('article/edit/<int:pk>/', edit_article, name='edit_article'),
    path('article/delete/<int:pk>/', delete_article, name='delete_article'),
    path('logout/',logout_user , name='logout'),
    path('login/',auth_view.LoginView.as_view(template_name='login.html') , name='login'),
    path('signup/', signup, name='signup'),
]

