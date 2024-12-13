from django.urls import path, include
from .views import ProfileView

urlpatterns = [
    # Auth views
     path('auth/reset/',include('django_rest_passwordreset.urls',namespace='password_reset')),
     # Profile views
    path('user/profile/',ProfileView.as_view(), name='user_profile'),
]