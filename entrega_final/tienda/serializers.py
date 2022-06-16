from dataclasses import fields
from unicodedata import category
from .models import Product, Sub_Category, Category, detalle_Categoria
from rest_framework import serializers


class CategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializers(serializers.ModelSerializer):
    Nombre_Categoria = serializers.CharField(read_only=True, source="category.nameCategory")

    id_Categoria = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source="category")
    
    class Meta:
        model = Sub_Category
        fields = '__all__'

class DetalleCategoriaSerializers(serializers.ModelSerializer):

    category = serializers.CharField(read_only=True, source="category.nameCategory")
    subCategory = serializers.CharField(read_only=True, source="subCategory.nameSubCategory")

    class Meta:
        model = detalle_Categoria
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):

    detalle = serializers.CharField(read_only=True, source="detalle.nombre")
    
    class Meta:
        model = Product
        fields = '__all__'





