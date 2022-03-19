from django.db import models
import re
from django.forms import BooleanField


EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
NAME_REGEX = re.compile(r"^[a-zA-Z-']+$")
PASS_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]{8,}$")

# Create your models here.
class valManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['nombre']) < 2:
            errors['nombre']= "El campo Nombre debe tener al menos 2 caracteres."

        if not NAME_REGEX.match(post_data['nombre']):
            errors['nombre']= "Caracteres invalidos en Nombre"

        if len(post_data['apellido']) < 3:
            errors["apellido"] = "El campo Apellido debe tener al menos 3 caracteres."
        
        if not NAME_REGEX.match(post_data['apellido']):
            errors['apellido']= "Caracteres invalidos en Apellido."
        
        if self.filter(username=post_data['username']).exists():
            errors["username"] = "username existente."
        
        if not EMAIL_REGEX.match(post_data['email']):
            errors["email"] = "Formato de email incorrecto"
        
        if self.filter(email=post_data['email']).exists():
            errors["email"] = "Email existente, revise si ya tiene un usuario creado."
        
        if post_data['password']!= post_data['confirmar_password']:
            errors["confirmar_password"] = "Las contraseñas no coinciden."
        
        return errors


class User(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=72)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=valManager()

    def __str__(self):
        return f" {self.nombre} {self.apellido} "

class FileManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['file_name']) < 4:
            errors['file_name']= "El proyecto debe tener al menos 4 caracteres"

        return errors

class File(models.Model):

    FORMATO_CHOICES = (
        ('-----------', '-----------'),
        ('Lider', 'Lider'),
        ('Express', 'Express'),
        ('SBA', 'SBA'),
        ('Mayorista', 'Mayorista'),
        ('Logistica', 'Logistica'),
        ('Omnicanalidad', 'Omnicanalidad'),
    )

    PROJ_TYPE_CHOICES = (
        ('-----------', '-----------'),
        ('Obra Nueva', 'Obra Nueva'),
        ('Remodelacion', 'Remodelacion'),
        ('Reconstruccion', 'Reconstruccion'),
        ('Roll-Out', 'Roll-Out'),
    )

    file_name = models.CharField(max_length=255)
    formato = models.CharField(max_length=100, choices=FORMATO_CHOICES, default='Z')
    store_number = models.IntegerField()
    proj_type = models.CharField(max_length=100, choices=PROJ_TYPE_CHOICES, default='Z')
    user = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE, null=True)
    added = models.BooleanField(default=False, null=True)
    complete = models.ManyToManyField(User, related_name='complete')
    uploaded_by=models.ForeignKey(User, related_name="upload_by", on_delete=models.CASCADE, null=True)
    #tasks = models.ManyToManyField(Task, related_name='task') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects=FileManager()

    def __str__(self):
        return self.file_name

class taskManager(models.Manager):
    
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['task']) < 10:
            errors['task']= "La tarea debe tener al menos 10 caracteres"

        return errors

class Task(models.Model):

    task = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    complete=models.ManyToManyField(File, related_name='completed')
    files=models.ManyToManyField(File, related_name='files')
    #rel1 
    objects=taskManager()

class Exp_task(models.Model):
    task=models.ForeignKey(Task,related_name='rel1' ,on_delete=models.CASCADE)
    file=models.ForeignKey(File,related_name='rel2', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="userss", on_delete=models.CASCADE, null=True)
    completado=models.BooleanField(default=False) #True=completado, False= no completado
    update_at=models.DateTimeField(auto_now=True)

    #tarea_target=Task.objects.get(id=1)
    #tarea_target.rel1.file[0].file_name
    


    objects=taskManager()

    def __str__(self):
        return self.task