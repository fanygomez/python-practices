from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
#Eliminar imagen antigua, y solo subir la nueva
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']
'''
Signals: Una señal es un disparador que se llama automáticamente después de un evento que ocurre en nuestro ORM.
En nuestro caso lo que haremos es crear automáticamente un perfil justo después de que se cree un usuario.
Donde:
@receiver: transforma la función en una señal cual le pasaremos, este recibe un tipo de señal, en nuestro caso post_save (después del guardado),
y un sender, que corresponderá al modelo encargado de enviar la señal, en nuestro caso User.
instance: Instance hace referencia al objeto/user que envia la se;al, es decir el usuario recién creado

'''
@receiver(post_save, sender=User) 
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False): #solo la primera vez que se crea la instancia ( excluye si es actualizacion)
        Profile.objects.get_or_create(user=instance)
        # print("Se acaba de crear un usuario y su perfil enlazado")