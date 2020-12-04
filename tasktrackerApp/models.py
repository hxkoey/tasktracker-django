from django.db import models
from datetime import datetime, timedelta

level_choice = (('Contract','Contract'),('Hire','Hire'),('Supervisor','Supervisor'))

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, choices=level_choice)

    def __str__(self):
        return self.name + ' ' + self.level

class Task(models.Model):
    task_name = models.CharField(max_length=100, blank=False, null=False)
    task_description = models.TextField(blank=True, null=True)
    date_start = models.DateField(auto_now=False, auto_now_add=True)
    date_due = models.DateField(auto_now=False, auto_now_add=False, default=datetime.today+timedelta(days=30), blank=True)
    assign_to = models.ForeignKey(Worker, db_column='name', on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
