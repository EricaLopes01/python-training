from django.shortcuts import render, redirect

from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'task_form.html')

def task_update(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'task_form.html', {'task': task})
