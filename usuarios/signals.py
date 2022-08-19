from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from usuarios.models import Datosusuario


@receiver(post_save, sender=User)
def create_datosusuario(sender, instance, created, **kwargs):
    if created:
        Datosusuario.objects.create(usuario=instance)


# @receiver(post_save, sender=User)
# def update_datosusuario(sender, instance, created, **kwargs):
#     if created == False:
#         instance.Datosusuario.save()

