from django.urls import path
from usuarios import views_login
from usuarios import views_logout
from usuarios import views_registro

urlpatterns = [
    path('login', views_login.pagina_login, name='login'),
    path('logout', views_logout.pagina_logout, name='logout'),
    path('registro', views_registro.pagina_registro, name='registro'),
]