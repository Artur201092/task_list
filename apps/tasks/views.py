from django.shortcuts import render

# Create your views here.
from django.views import View

from apps.tasks.models import Tasks
from tasklist.forms import TaskForm


class HomeView(View):
    form_class = Tasks
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = TaskForm
        tasks = Tasks.objects.all()
        return render(request, self.template_name, {'form': form, "tasks": tasks})


def add_task(request):
    form = TaskForm(request.POST)
    data = request.POST
    if form.is_valid():
        task = Tasks(name=data["name"], description=data["description"])
        task.save()
        tasks = Tasks.objects.all().order_by("-created_at")
        return render(request, 'home.html', {'form': form, 'tasks': tasks})


def get_task(request, pk=None):
        task = Tasks.objects.get(pk=pk)
        return render(request, 'task.html', {'task': task})


def delete_task(request, pk=None):
    task = Tasks.objects.get(pk=pk)
    task.delete()
    tasks = Tasks.objects.all()
    form = TaskForm
    return render(request, 'home.html', {'form': form, 'delete_success': True, 'tasks': tasks})