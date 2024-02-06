from django.urls import path
from .views import index, addtask, viewtasks,home, deletetask

urlpatterns = [
    path('',home, name='home'),
    path('index/', index , name='index'),
    path('addtask/', addtask, name='addtask'),
     path('tasks/', viewtasks, name='tasks'),
     path('deletetask/<int:task_id>/', deletetask, name='deletetask'), 
]