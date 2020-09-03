from django.contrib import admin
from .models import Task, TaskGroup
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'task_group')
    list_filter = ('status','task_group')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class TaskGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(Task, TaskAdmin)