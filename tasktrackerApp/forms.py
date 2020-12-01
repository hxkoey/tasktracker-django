from django import forms
from .models import *
from datetime import datetime

level_choice = (('','-------'),('Contract','Contract'),('Hire','Hire'),('Supervisor','Supervisor'))

class TaskAddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class WorkerAddForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'

class TaskSearchForm(forms.ModelForm):
    task = forms.CharField(max_length=100, required=False)
    assigned = forms.CharField(max_length=100, required=False)
    completed = forms.ChoiceField(choices=(('','-------'),('1','True'),('0','False')), required=False)
    employee_class = forms.ChoiceField(choices=level_choice, required=False)

    class Meta:
        model = Task
        fields = ['task', 'assigned', 'date_due', 'employee_class', 'completed',]
