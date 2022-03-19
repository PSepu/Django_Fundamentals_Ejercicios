from django.urls import path     
from . import views



urlpatterns =[
    path('', views.index, name='index'),
    path('create/', views.add_user, name='add_user'),
    path('login', views.login, name='login'),
    path('succed/', views.succed, name='succed'),
    #-------Tareas-----#
    path('createtask/', views.create_task, name='create_task'),
    path('tasks/', views.all_tasks, name='all_tasks'),
    path('edittask/<int:id>', views.edit_task, name='edit_task'),
    path('deletetask/<int:id>', views.delete_task, name='delete_task'),
    #-------Expedientes-----#
    path('createfile/', views.create_file, name='create_file'),
    path('files/', views.all_files, name='all_files'),
    path('deletefile/<int:id>', views.delete_file, name='delete_file'),
    path('files/<int:id>/complete/task/', views.task_complete, name='task_complete'),
]