from django.db import models
from django import forms
from .models import User
from datetime import datetime


class UserForm(forms.ModelForm):

    confirmar_password = forms.CharField(label="Confirmar Password", widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Repita su password'}))

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)

        if cleaned_data.get('password') != cleaned_data.get('confirmar_password'):
            raise forms.ValidationError(
                "Las contraseñas no coinciden"
            )

    class Meta:
        model = User
        fields=['nombre','apellido','username','email','password']

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su nombre aqui'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su apellido aqui'}),
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Elija un username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@ejemplo.com'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Elija un password seguro'}),
        }

class LoginForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)

        if cleaned_data.get('password') != cleaned_data.get('confirmar_password'):
            raise forms.ValidationError(
                "Las contraseñas no coinciden"
            )

    class Meta:
        model = User
        fields=['username','password']

        labels = {
            'username': 'Username',
            'password': 'Password',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su username' }),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su password'}),
        }


