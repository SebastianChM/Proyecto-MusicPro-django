import imp
from unicodedata import name
from django.db import router
from django.urls import path, include
from .views import categoria, contacto, eliminar_producto, home, index, agregar_producto, listar_productos, modificar_producto, registro, ProductViewset, CategoryViewset, SubCategoryViewset, DetalleCategoriaViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('producto', ProductViewset, basename='Producto'),
router.register('Categoria', CategoryViewset, basename='Categoria'),
router.register('sub_categoria', SubCategoryViewset, basename='sub_categoria'),
router.register('detalle_categoria', DetalleCategoriaViewset, basename='detalle_categoria')

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('index/', index, name='index'),
    path('categoria/', categoria, name='categoria'),
    path('contacto/', contacto, name='contacto'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('listar-producto/', listar_productos, name='listar_producto'),
    path('modificar-producto/<id>/', modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', eliminar_producto, name='elminar_producto'),
    path('registro/', registro, name='registro'),
    path('api/', include(router.urls))
]
