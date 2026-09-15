from django.shortcuts import render, redirect
from . import models
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).manage = request.user
            # request.user jest zalogowanym uzytkownikiem
            # commit=False oznacza, ze nie zapisujemy do bazy
            form.save()
            messages.success(request, 'Task added successfully')
        return redirect('todolist')
    else:
        # all_tasks = models.TaskList.objects.all()
        all_tasks = models.TaskList.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks, 5) # 5 tasks per page
        page = request.GET.get('pg') # page number from url
        all_tasks = paginator.get_page(page) # returns page object
    return render(request, 'home.html', {'all_tasks': all_tasks})

@login_required
def delete_task(request, task_id):
    #  task_id jest pobierane z url
    task = models.TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
        messages.success(request, 'Task added successfully')
    else:
        messages.error(request, 'You don\'t have permission to delete this task.')
    return redirect('home')

@login_required
def edit_task(request, task_id):
    task = models.TaskList.objects.get(pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task edited successfully')
            return redirect('home')
    return render(request, 'edit_task.html', {'task': task})

@login_required
def complete_task(request, task_id):
    task = models.TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, 'You don\'t have permission to edit this task.')
    return redirect('todolist') 

@login_required
def pending_task(request, task_id):
    task = models.TaskList.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, 'You don\'t have permission to edit this task.')
    return redirect('todolist')

def index(request):
    context = {
        'index_text':"Welcome Index Page.",
        }
    return render(request, 'index.html', context)
def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
