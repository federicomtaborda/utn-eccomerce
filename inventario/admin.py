from django.contrib import admin

from .models import Producto, Categoria

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):

    list_display = ['pk','nombre','descripcion','precio_venta', 'imagen', 'estado']
    search_fields=('nombre', 'descripcion')
    fieldsets = [
        ("Nombre del Producto", {"fields": ["nombre","descripcion"]}),
        ("Precios", {"fields": ["costo_colocacion","costo_envio","otros_costos","precio_venta"]}),
        ("Estado", {"fields": ["estado","fecha_create","imagen"]})
     ]

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields=('categoria', 'descripcion')
    list_display = ['pk','categoria','descripcion','estado']