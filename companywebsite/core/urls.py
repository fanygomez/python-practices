from django.contrib import admin
from django.urls import include, path
from . import views as core_views
urlpatterns = [
    # Path del core app
    path('', core_views.home, name="home"),
    path('about/', core_views.about, name="about"),
    path('store/', core_views.store, name="store"),
]
