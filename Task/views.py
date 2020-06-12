from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, UpdateForm
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    Tasks = Task.objects.all().order_by('-date_created')
    len_of_tasks = Task.objects.all().count()

    if request.method  == 'POST':
        form  = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-home')

    else:
        form = TaskForm()
        context = {'tasks': Tasks,'form': form, 'count': len_of_tasks}
    return render(request, 'task/home.html', context)





def deleteTask(request, pk):
    item  = Task.objects.get(id = pk).delete()
    return redirect('/')


def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        form  = UpdateForm(request.POST, instance= task)
        if form.is_valid():
            form.save()

            return redirect('task-home')
    else:
        form = UpdateForm(instance=task)
        context = {'tasks': task,'form': form}
    return render(request, 'task/task-update.html', context)
