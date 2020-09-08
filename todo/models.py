from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse # new
from autoslug import AutoSlugField


# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(default="")
   
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Task Lists"

class Task(models.Model):
    title = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from='title')
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(
        User,
        related_name="todo_created_by",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('task_detail', args=[str(self.slug)])
