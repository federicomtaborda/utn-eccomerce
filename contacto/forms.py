from django import forms
from django.forms import ModelForm
from contacto.models import Consulta
from django import forms
#from captcha.fields import CaptchaField

# pip install django-simple-captcha
class ConsultaForm(ModelForm):

    class Meta:
        model = Consulta
        fields = [
            "nombre",
            "descripcion",
            "mail",
            "telefono",
        ]