from django.urls import path
from tienda import views
from tienda.views import VerProductos

urlpatterns = [
    path('cargar/', views.cargar_imagen, name="cargar"),
    path('<int:producto_id>/ver/', views.ver_producto, name="ver"),  
    path('verproductos/', VerProductos.as_view(), name="verproductos"),
]