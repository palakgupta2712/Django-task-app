from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskList,Task
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin # new
from django.core.exceptions import PermissionDenied # new
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy # new


tasks = Task.objects.all()

# Create your views here.
def index(request):
    return render(request, 'index.html',{
        "tasks" : Task.objects.all().count(),
        "task_list" : TaskList.objects.all().count(),
    })

def home(request):
    return render(request, 'home.html')

def tasklist(request):
    lists = Task.objects.filter(task_list=1)
    count = lists.count()
    return render(request, 'tasklist.html', {
        "tasks_list" : TaskList.objects.all(),
        "count" : count
        
    })
    
@login_required
def tasks(request):
    return render(request, 'tasks.html',{
        "tasks" : Task.objects.all(),
        "task_group" : TaskList.objects.all(),
        "tasks_todo" : Task.objects.filter(completed="False").count(),
        "tasks_done" : Task.objects.filter(completed="True").count()
    }) 

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task 
    template_name = "task_new.html"
    fields = ['title', 'description',  'task_list', 'completed']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

@login_required
def task_detail(request, slug):
    tasks = Task.objects.get(slug=slug)
    return render(request, 'task_detail.html',{
        "tasks" : tasks
    })   
    
@login_required
def tasklist_details(request, tasklist_id):
    tasklist = TaskList.objects.get(pk=tasklist_id)
    lists = Task.objects.filter(task_list=tasklist_id)
    count = lists.count()
    return render(request, 'tasklist_details.html',{
        "tasklist" : tasklist,
        "lists" : lists,
        "tasks_todo" : lists.filter(completed="False").count(),
        "tasks_done" : lists.filter(completed="True").count()
    })     

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'task_edit.html'
    fields = ['title', 'description','task_list','completed']
    
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.created_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class TaskListCreate(LoginRequiredMixin, CreateView):
    model = TaskList 
    template_name = "tasklist_new.html"
    fields = '__all__'

class TaskListDelete(LoginRequiredMixin,DeleteView):
    model = TaskList
    template_name = "tasklist_delete.html"
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy('tasks')