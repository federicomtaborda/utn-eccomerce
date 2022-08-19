from django.contrib import admin

from .models import Datosusuario

# Register your models here.


@admin.register(Datosusuario)
class DatosusuarioAdmin(admin.ModelAdmin):
    list_display = ['pk','apellido','nombre', 'email']