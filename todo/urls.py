from django.urls import path
from . import views
urlpatterns =[
    path('', views.index, name='home'),
    # path('home/', views.home, name='home'),
    path('tasklist/', views.tasklist, name='tasklist'),
    path('task/', views.tasks, name='tasks'),
    path('task/add/', views.TaskCreate, name='tasks_add'),
    path('task/<slug:slug>/', views.task_detail, name='task_detail'),
    path('tasklist/<int:tasklist_id>/', views.tasklist_details, name='tasklist_detail'),
    path('task/<slug:slug>/edit/', views.TaskUpdate.as_view(), name='task_edit'),
    path('tasklist/add/', views.TaskListCreate.as_view(), name="tasklist_new"),
    path('post/<int:pk>/delete/', views.TaskListDelete.as_view(), name='tasklist_delete'),
    path('task/<slug:slug>/delete/', views.TaskDelete.as_view(), name='task_delete'),
    # path("toggle_done/<int:task_id>/", views.toggle_done, name="task_toggle_done"),

] 