from django.urls import path     
from . import views



urlpatterns =[
    path('', views.index, name='index'),
    path('create/', views.add_user, name='add_user'),
    path('login', views.login, name='login'),
    path('succed/', views.succed, name='succed'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout' ),
    path('books/', views.all_books, name='all_books'),
    path('show/<int:id>', views.show_book, name='show_book'),
    path('edit/<int:id>', views.edit_book, name='edit_book'),
    path('delete/<int:id>', views.delete_book, name='delete_book'),
    path('books/<int:id>/add/user/', views.user_add_book, name='user_add_book' ),
    path('books/<int:id>/remove/user/', views.user_remove_book, name='user_remove_book' ),
]
