from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskList,Task
from django.views import generic
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def tasklist(request):
    list_count = lists.count()
    return render(request, 'tasklist.html', {
        "tasks_list" : TaskList.objects.all(),
        "list" : lists
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
    fields = ['title', 'task_list', 'completed']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TaskDetail(generic.DetailView):
    model = Task
    template_name = 'task_detail.html'

def tasklist_details(request, tasklist_id):
    tasklist = TaskList.objects.get(pk=tasklist_id)
    lists = Task.objects.filter(task_list=tasklist_id)
    return render(request, 'tasklist_details.html',{
        "tasklist" : tasklist,
        "lists" : lists

    })     