# Generated by Django 3.1.2 on 2020-11-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktrackerApp', '0004_auto_20201130_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
