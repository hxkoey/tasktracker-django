# Generated by Django 3.1.3 on 2020-11-30 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktrackerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
