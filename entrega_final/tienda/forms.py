from tkinter import Widget
from django import forms
from .models import Contacto, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model    = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]