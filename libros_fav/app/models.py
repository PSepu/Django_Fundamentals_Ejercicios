from django.db import models
import re

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
    username = models.CharField(max_length=20, unique=True, verbose_name="Nombre de Usuario")
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=72)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=valManager()

    def __str__(self):
        return f" {self.nombre} {self.apellido} "

class BookManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 2:
            errors['title']= "El titulo debe tener al menos 2 caracteres"

        if len(post_data['desc']) < 10:
            errors['desc']= "Por favor, haz una reseña mas completa"

        return errors

class Book(models.Model):

    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by=models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users=models.ManyToManyField(User, related_name='users')

    objects=BookManager()

    def __str__(self):
        return self.title