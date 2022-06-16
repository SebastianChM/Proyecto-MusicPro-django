from distutils.command.upload import upload
from unicodedata import category, name
from django.db import models
from django.forms import CharField

# Create your models here.



class Category(models.Model):
    category = (
        ('Instrumentos de cuerdas', 'Cuerdas'),
        ('Instrumentos de percusión', 'Percusión'),
        ('Amplificadores para instrumentos', 'Amplificadores'),
        ('Accesorios varios para variados instrumentos', 'Accesorios varios')
    )
    nameCategory = models.CharField(max_length=50 , choices=category)

    def __str__(self):
        return self.nameCategory

class Sub_Category(models.Model):
    nameSubCategory = models.CharField(max_length=30)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nameSubCategory

class detalle_Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    nivel = models.IntegerField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    subCategory = models.ForeignKey(Sub_Category, null=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return self.nombre

class Product(models.Model):
    nameProduct = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    color = models.CharField(max_length=30)
    description = models.TextField()
    value = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(null=True)
    detalle = models.ForeignKey(detalle_Categoria, null=True, on_delete=models.SET_NULL)
    imagen = models.ImageField(upload_to="productos", null=True)


class Contacto(models.Model):
    opciones_consulta = [
        [0, "Consulta"],
        [1, "Reclamo"],
        [2, "Sugerencia"],
        [3, "Otro"]
    ]

    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
   
