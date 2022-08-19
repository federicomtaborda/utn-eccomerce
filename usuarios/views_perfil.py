from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from usuarios.models import Datosusuario

# Create your views here.

class ver_perfilusuario(View):
    template = "usuarios/perfil_usuario.html"

    def get(self, request):
        params = {}
        if request.user.is_authenticated:
            params["usuario"] = Datosusuario.objects.get(pk=request.user.pk)
        else:
            return redirect("login")
        return render(request, self.template, params)
