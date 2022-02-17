from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name="books"),
    path('books/remove/', views.book_remove, name="books_remove"),
    path('book/<int:id>/', views.book, name="book"),
    path('book/<int:id>/add/author/', views.book_add_author, name='book_add_author' ),
    path('book/<int:id>/remove/author/', views.book_remove_author, name='book_remove_author' ),
]
