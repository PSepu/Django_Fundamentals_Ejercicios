# Generated by Django 4.0.2 on 2022-03-04 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_user_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
    ]
