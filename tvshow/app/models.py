from __future__ import unicode_literals
from django.db import models

# Create your models here
class valManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 2:
            errors['title']= "Campo de titulo es obligatorio y debe tener al menos 2 caracteres"
        
        if len(post_data['network']) < 3:
            errors["network"] = "Campo de titulo es obligatorio y debe tener al menos 2 caracteres"

        if len(post_data['desc']) < 10:
            errors["desc"] = "La descripcion debe ser de al menos 10 caracteres"

        return errors

class Show(models.Model):
    title = models.CharField(max_length=200)
    network = models.CharField(max_length=200)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=valManager() 

class UserManager(models.Manager):
    def basic_validator_user(self, post_data):
        errors = {}

        if len(post_data['first_name']) < 2:
            errors['first_name']= "Campo de titulo es obligatorio y debe tener al menos 2 caracteres"
        
        if len(post_data['last_name']) < 3:
            errors["last_name"] = "Campo de titulo es obligatorio y debe tener al menos 2 caracteres"

        if self.filter(email=post_data['email']).exists():
            errors["email"] = "email existe."

        if post_data['password']!= post_data['confirmar_password']:
            errors["password"] = "las contraseñas no coinciden"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    birthday = models.DateTimeField()
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager() 