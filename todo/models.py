from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskGroup(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField()

    def __str__(self):
        return self.name


STATUS =(
    ("Todo", "Todo"),
    ("Done", "Done")
)
class Task(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name="created_by")
    status = models.TextField(choices=STATUS, default = "Todo")
    task_group = models.ForeignKey(TaskGroup, on_delete= models.CASCADE, related_name="task_group")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title