from django.urls import path

from inventario import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos',views.productos, name='productos')
]
