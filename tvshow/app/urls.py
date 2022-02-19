from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('create/', views.create, name='create'),
    path('shows/', views.all_shows, name='all_shows'),
    path('show/<int:id>', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]