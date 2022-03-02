from django.db import models

# Create your models here.
class valManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['nombre']) < 2:
            errors['nombre']= "El campo Nombre debe tener al menos 2 caracteres"
        
        if len(post_data['apellido']) < 3:
            errors["apellido"] = "El campo Apellido debe tener al menos 3 caracteres"

        if self.filter(username=post_data['username']).exists():
            errors["email"] = "username existente."

        if self.filter(email=post_data['email']).exists():
            errors["email"] = "Email existente, revise si ya tiene un usuario creado"

        if post_data['password']!= post_data['confirmar_password']:
            errors["password"] = "Las contraseñas no coinciden"

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