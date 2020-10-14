from django.forms import ModelForm
from .models import Task,TaskList

class TaskForm(ModelForm):  
    class Meta:  
        model = Task  
        exclude = ['completed_date', 'created_by','created_date'] 
                 # widgets = {'country': CountrySelectWidget()}
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['task_list'].queryset = TaskList.objects.filter(created_by=request.user)