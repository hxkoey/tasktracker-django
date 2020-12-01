from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    title = "Welcome to CRACKALACKA-TRACKAAAR"
    queryset = Task.objects.all().values('id', 'task_name', 'date_start', 'date_due', 'complete', 'assign_to', 'assign_to__name')
    form = TaskSearchForm

    if request.method == 'POST':
        form = TaskSearchForm(request.POST)

        date_start = "2010-01-01"
        date_to = ['2030-01-01' if form['date_due'].value() == '' else form['date_due'].value()][0]
        queryset = Task.objects.all().values('id', 'task_name', 'date_start', 'date_due', 'complete', 'assign_to', 'assign_to__name')\
        .filter(task_name__icontains = form['task'].value(),
        assign_to__name__icontains = form['assigned'].value(),
        complete__icontains = form['completed'].value(),
        assign_to__level__icontains = form['employee_class'].value(),
        date_due__range = [date_start, date_to]
        )

    # Create table with pages
    p = Paginator(queryset, 5)
    page_num = request.GET.get('page',1)

    try:
        page = p.page(page_num)
    except:
        page = p.page(1)

    context = {'title':title, 'form': form, 'page': page}
    return render(request, 'tasktrackerApp/index.html', context)

def add_task(request):
    title = "Add Task Form Below"
    form = TaskAddForm

    if request.method == 'POST':
        form = TaskAddForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Task added succesfully.')
            return redirect('/')

    context = {'title': title, 'form': form}
    return render(request, 'tasktrackerApp/add_task.html', context)

def add_worker(request):
    title = "Add worker"
    form = WorkerAddForm

    if request.method == 'POST':
        form = WorkerAddForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Worker added successfully")
            return redirect('/')

    context = {'title': title, 'form': form}
    return render(request, 'tasktrackerApp/add_worker.html', context)

def list_workers(request):
    title = "List of CRACKALACKA-EEEEE"
    queryset = Worker.objects.all()

    context = {'title': title, 'queryset': queryset}
    return render(request, 'tasktrackerApp/list_workers.html', context)

def delete_worker(request, pk):
    title = 'Are you sure you want to delete employee?'
    queryset = Worker.objects.get(id=pk)

    if request.method == 'POST':
        queryset.delete()
        messages.success(request,'Employee deleted successfully')
        return redirect('/list_workers')

    context = {'title':title}
    return render(request, 'tasktrackerApp/delete_worker.html', context)

def update_items(request, pk):
    title = 'Update Task'
    queryset = Task.objects.get(id=pk)
    form = TaskAddForm(instance=queryset)

    if request.method == 'POST':
        form = TaskAddForm(request.POST, instance=queryset)
        form.save()
        messages.success(request, 'Task updated successfully.')
        return redirect('/')


    context = {'title':title, 'form':form}
    return render(request, 'tasktrackerApp/add_worker.html', context)
