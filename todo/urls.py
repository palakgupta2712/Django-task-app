from django.urls import path
from . import views
urlpatterns =[
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('tasklist/', views.tasklist, name='tasklist'),
    path('task/', views.tasks, name='tasks'),
    path('task/add/', views.TaskCreate.as_view(), name='tasks_add'),
    path('task/<slug:slug>/', views.TaskDetail.as_view(), name='task_detail'),
    path('<int:tasklist_id>/', views.tasklist_details, name='tasklist_detail'),

] 