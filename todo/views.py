from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm
from .models import Task
from django.urls import reverse
from django.http import HttpResponseRedirect

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_add(request):
    if request.method == 'GET':
            form = TaskForm()
            return render(request, "todo/task_form.html", {'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                description=form.cleaned_data.get('description', ''),
                status=form.cleaned_data.get('status', 'new'),
                due_date=form.cleaned_data.get('due_date') or None,
                detail_descriptions=form.cleaned_data.get('detail_descriptions') or None,
            )
            return HttpResponseRedirect(reverse('task_detail', kwargs={'task_id': task.pk}))
        else:
            return render(request, "todo/task_form.html", {'form': form})

def task_delete(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    return HttpResponseRedirect(reverse('task_list'))

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'todo/task_detail.html', {'task': task})

def task_update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.detail_descriptions = form.cleaned_data['detail_descriptions'] or None
            task.status = form.cleaned_data['status']
            task.due_date = form.cleaned_data['due_date']
            task.save()
            return redirect('task_detail', task_id=task.pk)
    else:
        form = TaskForm(initial={
            'description': task.description,
            'detail_descriptions': task.detail_descriptions,
            'status': task.status,
            'due_date': task.due_date,
        })

    return render(request, 'todo/task_update.html', {
        'task': task,
        'form': form,
    })
