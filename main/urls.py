"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from principal.views import index, reserva_criar, reserva_editar, reserva_listar, reserva_remover, stand_criar, stand_editar, stand_listar, stand_remover


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('reserva/',reserva_criar,name='reserva_criar'),
    path('reserva/editar/<int:id>/',reserva_editar, name='reserva_editar'),
    path('reserva/remover/<int:id>/',reserva_remover,name='reserva_remover'),
    path('reserva/listar',reserva_listar,name='reserva_listar'),

    path('stand/',stand_listar, name ='stand_listar'),
    path('stand/criar', stand_criar, name= 'stand_criar' ),
    path('stand/editar/<int:id>/',stand_editar, name='stand_editar'),
    path('stand/remover/<int:id>/',stand_remover,name='stand_remover'),
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
