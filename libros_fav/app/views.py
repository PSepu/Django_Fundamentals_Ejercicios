from django.shortcuts import render, HttpResponse
from app.forms import RegistroUsuario

def index(request):
    return render(request, 'index.html')


