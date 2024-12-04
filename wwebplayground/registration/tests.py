from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self): # Este metodo, se ejecuta antes de cada prueba y sirve para preparar el entorno (por ejemplo, crear mocks u objt de prueba).
        # Crear un usuario y un perfil
        self.user = User.objects.create_user(username="fanny", email="fany.gomez@test.com",password="password123")
        self.profile = Profile.objects.get(user__email=self.user.email)

    def test_profile_bio_update(self):
        # Obtener el perfil asociado al usuario
        profile = Profile.objects.get(user=self.user)

        # Actualizar la bio
        profile.bio = "Updated bio"
        profile.save()

        # Verificar que el cambio se haya guardado
        updated_profile = Profile.objects.get(user=self.user)
        self.assertEqual(updated_profile.bio, "Updated bio")
        
    def test_profile_exists(self):
        # Verifica que el perfil se creó correctamente
        exists = Profile.objects.filter(user__username='fanny').exists()

        self.assertEqual(exists, 1)

        