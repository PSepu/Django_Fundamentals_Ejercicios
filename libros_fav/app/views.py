from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import User, Book
from .forms import UserForm, LoginForm, BookForm
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
                request.session['username'] = log_user.username
                request.session['nombre'] = log_user.nombre

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

        contexto = {
            'BookForm' : BookForm(),
            'books': Book.objects.filter(uploaded_by=User.objects.get(id=request.session['user']['id']))

        }
        return render(request, 'home.html', contexto)
    if request.method == "POST":
        print(request.POST)

        errors = Book.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
            
            return redirect ('home')
        
        else:
            contexto = {
                'BookForm' : BookForm(),
                'books': Book.objects.filter(uploaded_by=User.objects.get(id=request.session['user']['id']))
            }

            Book.objects.create(
                title=request.POST['title'],
                desc=request.POST['desc'],
                uploaded_by=User.objects.get(id=request.session['user']['id']),
            )
            
            return render(request, 'home.html', contexto)


def logout(request):
    if 'user' in request.session:
        del request.session['user']
    
    return redirect("/login")

def all_books(request):
    if request.method == "GET":
        contexto = {
            'books': Book.objects.exclude(users=User.objects.get(id=request.session['user']['id'])),
            'favoritos': Book.objects.filter(users=User.objects.get(id=request.session['user']['id'])),
        }

        return render(request, 'all_books.html', contexto)

def show_book(request, id):
    if request.method == "GET":
        contexto = {
            'books': Book.objects.get(id=id),
            'favoritos': User.objects.filter(users=Book.objects.get(id=id)),
        }
        return render(request, 'libro.html', contexto)


def edit_book(request, id):
    
    book = Book.objects.get(id=id)

    if request.method == 'GET':
        contexto = {
            'books' : book
        }
        return render(request, 'book_edit.html',contexto)
    
    if request.method == "POST":
        print(request.POST)
        
        errors = Book.objects.basic_validator(request.POST)

        if len(errors)> 0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect (f'/edit/{id}') 
        
        else:
            book.title = request.POST['title']
            book.desc = request.POST['desc']  
            book.save()
        
    return redirect(reverse('home'))

def delete_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'books' : book
        }
        return render(request,'confirm_delete_book.html', contexto)
    if request.method == 'POST':
        book.delete()
    return redirect(reverse('home'))

def user_add_book(request, id):

    #print(request.POST)

    este_users = User.objects.get(id=request.session['user']['id'])
    este_book = Book.objects.get(id=id)
    print(este_users)

    este_book.users.add(este_users)
    este_book.save()

    return redirect('all_books')


def user_remove_book(request, id):

    print(request.POST)

    este_users = User.objects.get(id=request.session['user']['id'])
    este_book = Book.objects.get(id=id)

    este_book.users.remove(este_users)

    return redirect('all_books')