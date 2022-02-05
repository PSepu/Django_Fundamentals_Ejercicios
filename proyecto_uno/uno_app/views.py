from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("hola mundo, puta madre que costo")

def root(request):
    return HttpResponse("Placeholder para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("Placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse("Placeholder para mostrar el blog numero" + number)

def edit(request, number):
    return HttpResponse("Placeholder para editar el blog numero" + number)

def destroy(request,number):
    return redirect('/blog')
