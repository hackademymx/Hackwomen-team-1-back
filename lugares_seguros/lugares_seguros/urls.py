"""lugares_seguros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('initial.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Con esta línea le digo al servidor django que cuando nos manden un media_url, que acceda al documento media_root (que es una carpeta en la que se pueden mandar imágenes). va a empezar a existir cuando agreguemos una imagen al servidor o se puede hacer de forma manual 

