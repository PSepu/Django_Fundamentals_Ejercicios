# Generated by Django 4.0.2 on 2022-03-04 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceso_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime),
        ),
    ]
