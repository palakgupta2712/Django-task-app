from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskList 
# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")


def tasklist(request):
    return render(request, 'tasklist.html', {
        "task_list" : TaskList.objects.all()
    }) 
