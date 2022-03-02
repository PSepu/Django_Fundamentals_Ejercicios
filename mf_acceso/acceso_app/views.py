from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm, LoginForm
from django.contrib import messages
from django.urls import reverse
import bcrypt

# Create your views here.
def index(request):

    return render(request, 'index.html')

def add_user(request):

    if request.method == 'GET':

        contexto = {
            'form' : UserForm(),
            'LoginForm' : LoginForm()
        }
        return render(request, 'register.html', contexto)

    if request.method == "POST":
        print(request.POST)

        form = UserForm(request.POST)

        if form.is_valid():
            #form.save()
            #Hasta que se pueda arreglar el Bcrypt
            usuario = form.save(commit=False) 
            usuario.password = bcrypt.hashpw(usuario.password.encode(), bcrypt.gensalt()).decode()
            usuario.save()

            messages.success(request, 'Usuario creado correctamente')
            return redirect(reverse('succed'))
        else:
            
            contexto = {
            'form' : UserForm(),
            'LoginForm' : LoginForm()
            }

        errors = User.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
            
            return render(request, 'register.html', contexto)   

def login(request):
    if request.method == "POST":
        print(request.POST)
        user = User.objects.filter(username=request.POST['username'])
        if user:
            log_user = user[0]

            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):

                user = {
                    "id" : log_user.id,
                    "nombre": f"{log_user.nombre}",
                    "apellido": f"{log_user.apellido}",
                    "email": log_user.email,

                }

                request.session['user'] = user
                messages.success(request, "Logueado correctamente.")
                #username=request.session['username']['name']
                return redirect("home")
            else:
                messages.error(request, "Password o Username  incorrectos.")
        else:
            messages.error(request, "Username o password incorrectos.")

        return redirect('login')

    else:
        contexto = {
        'form' : UserForm(),
        'LoginForm' : LoginForm()
        }
        return render(request, 'register.html', contexto)  


def succed(request):
    if request.method == "GET":
        return render(request, 'succed.html')

def home(request):
    if request.method == "GET":
        return render(request, 'home.html')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    
    return redirect("/login")
