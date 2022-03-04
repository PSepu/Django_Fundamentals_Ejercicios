# Generated by Django 4.0.2 on 2022-03-03 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_users_who_like_book_users_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='users_like',
        ),
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(related_name='users', to='app.User'),
        ),
    ]
