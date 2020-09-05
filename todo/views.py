from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskList,Task
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")


def tasklist(request):
    return render(request, 'tasklist.html', {
        "task_list" : TaskList.objects.all()
    }) 
    
def tasks(request):
    return render(request, 'tasks.html', {
        "tasks" : Task.objects.all(),
        "tasks_todo" : Task.objects.filter(completed="False").count(),
        "tasks_done" : Task.objects.filter(completed="True").count()

    }) 

class TaskCreate(CreateView):
    model = Task 
    template_name = "task_new.html"
    fields = "__all__"

