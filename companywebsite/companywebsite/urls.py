"""
URL configuration for companywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from companywebsite import settings
urlpatterns = [
    # Path del core app
    path('', include('core.urls')),
    #Path services app
    path('services/',include('services.urls') , name="services"),
    #Path blog app
    path('blog/',include('blog.urls') , name="blog"),
    # Path page app
    path('page/', include('pages.urls')),
    #Page Contact
    path('contact/', include('contact.urls')),
    # Paths del admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)