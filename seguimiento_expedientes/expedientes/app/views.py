from django.shortcuts import render, redirect
from .models import User, Task, File, Exp_task
from .forms import UserForm, LoginForm, TaskForm, FileForm
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

                return redirect("all_files")
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

#----------------------------Expedientes----------------------------------------------#

def all_files(request):
    user=User.objects.get(id=request.session['user']['id'])
    if request.method == "GET":
        contexto = {
            'user' : User.objects.get(id=request.session['user']['id']),
            'files': File.objects.all().order_by('-updated_at'),
            'tasks': Task.objects.all().order_by('updated_at'),
        }
        return render(request, 'all_files.html', contexto)

def my_files(request):
    user=User.objects.get(id=request.session['user']['id'])
    if request.method == "GET":
        contexto = {
            'user' : User.objects.get(id=request.session['user']['id']),
            'files': File.objects.all().order_by('-updated_at').exclude(add=User.objects.get(id=request.session['user']['id'])),
        #    'addedjobs': Job.objects.filter(add=User.objects.get(id=request.session['user']['id'])),
        }
        return render(request, 'all_files.html', contexto)

def create_file(request):
    if request.method == "GET":

        contexto = {
            'FileForm' : FileForm(),
    }
        return render(request, 'create_file.html', contexto)


    if request.method == "POST":
        print(request.POST)

        errors = File.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
            
            return redirect ('create_file')
        
        else:
            file_nuevo=File.objects.create(
                file_name = request.POST['file_name'],
                formato = request.POST['formato'],
                store_number = request.POST['store_number'],
                proj_type = request.POST['proj_type'],
                user=User.objects.get(id=request.session['user']['id']),

            )
            tareas=Task.objects.all()

            for t in tareas:
                Exp_task.objects.create(task=t,file=file_nuevo)


        return redirect("all_files")

def delete_file(request, id):
    file = File.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'file' : file
        }
        return render(request,'confirm_delete_file.html', contexto)
    if request.method == 'POST':
        file.delete()
    return redirect(reverse('all_files'))

def task_complete(request, id):

    #print(request.POST)

    este_file = File.objects.get(id=id)
    este_task = Task.objects.get(id=id)
    print(este_file)

    este_task.complete.add(este_file)
    este_task.save()

    return redirect('all_files')

#----------------------------Tareas----------------------------------------------#
def create_task(request):
    if request.method == "GET":

        contexto = {
            'TaskForm' : TaskForm(),
    }
        return render(request, 'create_task.html', contexto)


    if request.method == "POST":
        print(request.POST)

        errors = Task.objects.basic_validator(request.POST)

        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
            
            return redirect ('create_task')
        
        else:
            Task.objects.create(
                task = request.POST['task'],
            )
        return redirect("all_tasks")

def all_tasks(request):
    user=User.objects.get(id=request.session['user']['id'])
    if request.method == "GET":
        contexto = {
            'tasks': Task.objects.all().order_by('updated_at'),
        }
        return render(request, 'all_tasks.html', contexto)

def edit_task(request, id):
    
    task = Task.objects.get(id=id)

    if request.method == 'GET':
        contexto = {
            'task' : task
        }
        return render(request, 'edit_task.html',contexto)
    
    if request.method == "POST":
        print(request.POST)
        
        errors = Task.objects.basic_validator(request.POST)

        if len(errors)> 0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect (f'/edit/{id}') 
        
        else:
            task.task = request.POST['task']
            task.save()
        
    return redirect(reverse('all_tasks'))

def delete_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'task' : task
        }
        return render(request,'confirm_delete_task.html', contexto)
    if request.method == 'POST':
        task.delete()
    return redirect(reverse('all_tasks'))