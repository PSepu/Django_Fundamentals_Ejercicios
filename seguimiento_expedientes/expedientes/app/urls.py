from django.urls import path     
from . import views



urlpatterns =[
    path('', views.index, name='index'),
    path('create/', views.add_user, name='add_user'),
    path('login', views.login, name='login'),
    path('succed/', views.succed, name='succed'),
    path('logout', views.logout, name='logout' ),
    #-------Tareas-----#
    path('createtask/', views.create_task, name='create_task'),
    path('tasks/', views.all_tasks, name='all_tasks'),
    path('edittask/<int:id>', views.edit_task, name='edit_task'),
    path('deletetask/<int:id>', views.delete_task, name='delete_task'),
    path('completetask/<int:id>', views.complete_task, name='complete_task'),
    #-------Expedientes-----#
    path('createfile/', views.create_file, name='create_file'),
    path('files/', views.all_files, name='all_files'),
    path('filesmy/', views.all_my_files, name='all_my_files'),
    path('deletefile/<int:id>', views.delete_file, name='delete_file'),
    path('editfile/<int:id>', views.edit_file, name='edit_file'),
]