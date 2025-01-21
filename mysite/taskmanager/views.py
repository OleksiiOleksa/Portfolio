# taskmanager/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse


def task_list(request):
    sort_by = request.GET.get('sort_by', 'created_at')  # По умолчанию сортировка по дате создания
    tasks = Task.objects.all().order_by(sort_by)
    return render(request, 'taskmanager/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'taskmanager/task_form.html', {'form': form})

def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.is_completed = not task.is_completed
        task.save()
        return redirect('task_list')
    return render(request, 'taskmanager/task_update.html', {'task': task})

def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.is_completed = not task.is_completed
        task.save()
        return JsonResponse({'status': 'Completed' if task.is_completed else 'Not Completed'})
    return redirect('task_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})