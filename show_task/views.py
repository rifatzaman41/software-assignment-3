from django.shortcuts import render, get_object_or_404, redirect
from add_task.models import TaskModel
from add_task.forms import TaskForm

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show.html', {'tasks': tasks})

def complete_task(request, task_title):
    task = get_object_or_404(TaskModel, id=task_title)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')

def edit_task(request, task_title):
    task = get_object_or_404(TaskModel, id=task_title)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task_title)
    return render(request, 'show.html', {'form': form})
