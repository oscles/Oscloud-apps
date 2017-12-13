"""oscloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from apps import helpers

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^proyecto/', include('apps.proyectos.urls', namespace='proyecto')),
    url(r'^cliente/', include('apps.clientes.urls', namespace='cliente')),
    url(r'^empleado/', include('apps.empleados.urls', namespace='empleado')),
    url(r'^evento/', include('apps.eventos.urls', namespace='evento')),
    url(r'^blog/', include('apps.blog.urls', namespace='blog')),

    url(r'^accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),

    #urls de la web
    url(r'^$', helpers.oscloud, {'template': 'index.html'}, name='inicio'),
    url(r'^nosotros/$', helpers.oscloud, {'template': 'aboutus.html'}, name='nosotros'),
    url(r'^servicios/$', helpers.oscloud, {'template': 'service.html'}, name='servicios'),
    url(r'^portafolio/$', helpers.oscloud, {'template': 'portfolio.html'}, name='portafolio'),
    url(r'^blogs/$', helpers.oscloud, {'template': 'blog.html'}, name='blog'),
    url(r'^contacto/$', helpers.oscloud, {'template': 'contact2.html'}, name='contacto'),


    #desde aqui van las url de prueba de la administración
    url(r'^contactos/miembros/$', helpers.oscloud, {'template': 'admin_oscloud/contactos_miembros.html'}, name='contactos'),
    url(r'^detalles/proyecto/$', helpers.oscloud, {'template': 'admin_oscloud/detalle_proyecto.html'}, name='detalle-proyectos'),
    url(r'^proyectos/cliente/$', helpers.oscloud, {'template': 'admin_oscloud/proyectos-cliente.html'}, name='proyectos-empleados'),
]



