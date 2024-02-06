# todolist/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import task
from .forms import TaskForm

def index(request):
    tasks = task.objects.all()
    form = TaskForm()
    return render(request, 'index.html', {'tasks': tasks, 'form': form})

def addtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['new_task']
            task.objects.create(title=title)
    return redirect('index')

def viewtasks(request):
    tasks = task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

def home(request):
    return render(request,'home.html')

def deletetask(request, task_id):
    tasks = get_object_or_404(task, pk=task_id)
    tasks.delete()
    return redirect('tasks')
