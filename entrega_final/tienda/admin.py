from django.contrib import admin
from .models import Product, Category, Sub_Category, detalle_Categoria, Contacto
# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(detalle_Categoria)
admin.site.register(Contacto)
