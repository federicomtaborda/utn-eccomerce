from email.mime import image
from django.db import models
from datetime import datetime

from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=100, unique=True, verbose_name='Producto')
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name='Descripción del Producto')
    estado = models.BooleanField(default=True, verbose_name='Estado del Producto')

    def __str__(self):
        return self.categoria

class Meta:
       verbose_name = 'Categoria'
       verbose_name_plural = 'Categorias'
       ordering = ['categoria']



class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Producto', unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name='Descripción de Producto')
    costo_colocacion = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, null=False, blank=False, verbose_name='Costo de Colocación')
    costo_envio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, null=False, blank=False, verbose_name='Costo de Envío')
    otros_costos = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, null=False, blank=False, verbose_name='Costo Costos')
    precio_venta = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, null=False, blank=False, verbose_name='Precio de Venta')
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True) 
    estado = models.BooleanField(default=True, verbose_name='Estado del Producto')
    fecha_create = models.DateField(default=datetime.now, verbose_name='Fecha')
    
    def __str__(self):
        return self.nombre


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']