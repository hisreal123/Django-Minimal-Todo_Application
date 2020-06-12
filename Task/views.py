from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

def home(request):
    Tasks = Task.objects.all().order_by('-date_created')
    form = TaskForm()

    if request.method  == 'POST':
        form  = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-home')
    context = {'tasks': Tasks,'form': form}

    return render(request, 'task/home.html', context)

def deleteTask(request, pk):
    item  = Task.objects.get(id = pk).delete()
    return redirect('/')