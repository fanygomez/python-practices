from django.urls import path
from .views import HomeView, SampleView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('sample/', SampleView.as_view(), name="sample"),
]