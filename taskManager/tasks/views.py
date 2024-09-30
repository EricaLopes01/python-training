from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task
from .forms import CustomUserCreationForm
from django.contrib.auth import login


@login_required
def task_list(request):
    
    if request.user.is_superuser:
        pending_tasks = Task.objects.filter(completed=False)
        completed_tasks = Task.objects.filter(completed=True)
    else:
        
        pending_tasks = Task.objects.filter(completed=False, assigned_to=request.user)
        completed_tasks = Task.objects.filter(completed=True, assigned_to=request.user)

    return render(request, 'tasks/task_list.html', {
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks
    })


@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        
        if request.user.is_superuser:
            assigned_to_username = request.POST.get('assigned_to')
            assigned_to_user = User.objects.filter(username=assigned_to_username).first() if assigned_to_username else request.user
        else:
            assigned_to_user = request.user  

        if title:
            Task.objects.create(title=title, created_by=request.user, assigned_to=assigned_to_user)
        return redirect('task_list')

   
    if request.user.is_superuser:
        users = User.objects.exclude(username=request.user.username)
    else:
        users = None 

    return render(request, 'tasks/add_task.html', {'users': users})


@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.created_by == request.user or task.assigned_to == request.user:
        task.completed = True
        task.save()
    return redirect('task_list')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False 
            user.save()
            login(request, user)  
            return redirect('task_list') 
    else:
        form = CustomUserCreationForm()

    return render(request, 'tasks/register.html', {'form': form})
