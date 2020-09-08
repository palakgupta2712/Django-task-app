from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse # new
from autoslug import AutoSlugField
from django.utils import datetime_safe



# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=60)
    slug = AutoSlugField(populate_from='name')
   
    def __str__(self):
        return self.name

    def get_absolute_url(self): # new
        return reverse('tasklist_detail', args=[str(self.id)])
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Task Lists"
    

class Task(models.Model):
    title = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(default='',blank=True)
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

# def get_attachment_upload_dir(instance, filename):
#     """Determine upload dir for task attachment files.
#     """
#     return "/".join(["tasks", "attachments", str(instance.task.id), filename])


# class Attachment(models.Model):
#     """
#     Defines a generic file attachment for use in M2M relation with Task.
#     """
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     added_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(default=timezone.now)
#     file = models.FileField(upload_to=get_attachment_upload_dir, max_length=255)

#     def filename(self):
#         return os.path.basename(self.file.name)

#     def extension(self):
#         name, extension = os.path.splitext(self.file.name)
#         return extension

#     def __str__(self):
#         return f"{self.task.id} - {self.file.name}"