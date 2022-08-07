from django.forms import ModelForm
from inventario.models import Producto
from django import forms

class CargarForm(ModelForm):
    class Meta:
        model=Producto
        fields = ['nombre', 'descripcion', 'precio_venta', 'imagen']

def __init__(self, *args, **kwargs):
        super(CargarForm, self).__init__(*args, **kwargs)
