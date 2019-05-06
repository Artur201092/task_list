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
    data = request.POST
    form = TaskForm(data={"name": data.get("name"), "description": data.get("description")})
    tasks = Tasks.objects.all().order_by("-created_at")
    if form.is_valid():
        task = Tasks(name=data["name"], description=data["description"])
        task.save()
        return render(request, 'home.html', {'form': form, 'tasks': tasks})
    return render(request, 'home.html', {'form': form, 'tasks': tasks})


def get_task(request, pk=None):
        task = Tasks.objects.get(pk=pk)
        return render(request, 'task.html', {'task': task})


def delete_task(request, pk=None):
    task = Tasks.objects.filter(pk=pk).first()
    if task:
        task.delete()
    tasks = Tasks.objects.all()
    form = TaskForm
    return render(request, 'home.html', {'form': form, 'delete_success': True, 'tasks': tasks})


def search_tasks(request):
    search_query = request.GET.get("search_query", None)
    tasks = Tasks.objects.filter(name__icontains=search_query)
    return render(request, "search_results.html", {"tasks": tasks, "search_keyword": search_query})

