# Generated by Django 3.1.2 on 2020-12-04 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktrackerApp', '0007_auto_20201204_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_due',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 1, 3, 21, 22, 8, 25681)),
        ),
    ]
