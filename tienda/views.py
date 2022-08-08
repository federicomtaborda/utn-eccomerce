from django.shortcuts import render
from django.http import Http404
from django.views.generic import View
from tienda.forms import CargarForm
from inventario.models import Producto


# Create your views here.

def cargar_producto(request):
    params={}

    if request.method == 'POST':
        form = CargarForm(request.POST, request.FILES)
        params['form']=form
        if form.is_valid():
                nombre = form.cleaned_data['nombre']
                descripcion = form.cleaned_data['descripcion']
                precio_venta = form.cleaned_data['precio_venta']
                imagen = form.cleaned_data['imagen']

                nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, precio_venta=precio_venta, imagen=imagen)
                nuevo_producto.save()
                return render(request, 'tienda/cargar_productos.html')

    else:
        form = CargarForm()
        params['form'] = form
        return render(request, 'tienda/cargar_productos.html', params)


class VerProductos(View):
    template = "tienda/productos.html"

    def get(self, request):
        params={}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"] = productos
        
        return render(request, self.template, params)


def ver_producto(request, producto_id):
    params={}
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404
    params["producto"] = producto
    
    return render(request, "tienda/ver_producto.html", params)
