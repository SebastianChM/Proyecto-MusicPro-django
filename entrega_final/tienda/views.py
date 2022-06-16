from itertools import product
from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Sub_Category, Category, detalle_Categoria
# Create your views here.
from django.shortcuts import render
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import CategorySerializers, DetalleCategoriaSerializers, ProductSerializers, SubCategorySerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tienda import serializers
# Create your views here.


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class SubCategoryViewset(viewsets.ModelViewSet):
    queryset = Sub_Category.objects.all()
    serializer_class = SubCategorySerializers

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class DetalleCategoriaViewset(viewsets.ModelViewSet):
    queryset = detalle_Categoria.objects.all()
    serializer_class = DetalleCategoriaSerializers



def home(request):
    productos = Product.objects.all()
    data = {
        'productos':productos
    }

    return render(request, 'tienda/home.html', data)

def index(request):
    return render(request, 'tienda/index.html')

def categoria(request):
    productos = Product.objects.all()
    data = {
        'productos':productos
    }
    return render(request, 'tienda/categoria.html', data)

def contacto(request):
    data = {
        'form':ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto enviado"
        else:
            data["form"] = formulario

    return render(request, 'tienda/contacto.html', data)

@permission_required('tienda.add_product')
def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto registrado correctamente!")
            data["mensaje"] = "Producto guardado correctamente!"
        else:
            data["form"] = formulario

    return render(request, 'tienda/producto/agregar.html', data)

@permission_required('tienda.view_product')
def listar_productos(request):

    productos = Product.objects.all

    data = {
        'productos': productos
    }

    return render(request, 'tienda/producto/listar.html', data)
 
@permission_required('tienda.change_product')
def modificar_producto(request, id):

    producto  = get_object_or_404(Product, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente!")
            return redirect(to="listar_producto")
            
        
        data["form"] = formulario
 

    return render(request, 'tienda/producto/modificar.html', data)

@permission_required('tienda.delete_product')
def eliminar_producto(request, id):

    producto = get_object_or_404(Product, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente!")
    return redirect(to="listar_producto")
 
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)