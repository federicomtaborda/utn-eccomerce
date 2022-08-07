from django import views
from django.shortcuts import render


# Create your views here.
def index(request):
    params = {}
    params['titulo_index'] = 'Bienvenido a Orsero Cortinas'
    return render(request, 'inventario/index.html', params)

def productos(request):
    return render(request, 'inventario/productos.html')

def contacto(request):
    return render(request, 'inventario/contacto.html')