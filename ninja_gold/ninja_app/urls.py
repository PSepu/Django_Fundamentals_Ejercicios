from django.urls import path
from . import views

app_name = 'ninja_app'

urlpatterns = [
    path('', views.index), 
    path('money',views.money, name='money'),
    path('index',views.index, name='index'),
    path('reset',views.reset, name='reset'),
    path('time',views.time, name="tiempo"),
]
