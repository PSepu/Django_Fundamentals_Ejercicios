from django.urls import path     
from . import views



urlpatterns =[
    path('', views.index, name='index'),
    path('create/', views.add_user, name='add_user'),
    path('login', views.login, name='login'),
    path('succed/', views.succed, name='succed'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout' ),
]
