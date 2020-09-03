from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Task
# Create your views here.

class TaskList(ListView):
    queryset = Task.objects.all().order_by('-created_on')
    template_name = 'TaskList.html'

