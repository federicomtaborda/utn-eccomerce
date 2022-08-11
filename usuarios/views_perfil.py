from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect

# Create your views here.

class ver_perfilusuario(View):
    template = "usuarios/perfil_usuario.html"

    def get(self, request):
        params = {}
        if request.user.is_authenticated:
            params["usuario"] = request.user
        else:
            return redirect("verproductos")
        return render(request, self.template, params)