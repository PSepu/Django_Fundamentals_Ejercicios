# Generated by Django 4.0.2 on 2022-03-18 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_file_task_delete_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='uploaded_by',
        ),
    ]
