from django.shortcuts import redirect, render
#from usuarios.forms import CreateUserForm

def pagina_registro(request):
    params={}
    # form=CreateUserForm()
    # params["form"]=form

    # if request.method =="POST":
    #     form=CreateUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("login")
    return render(request, "usuarios/registro.html", params)
