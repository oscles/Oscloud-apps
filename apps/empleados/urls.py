from django.conf.urls import url

from apps.empleados.views import (
    HabilidadCreateView,
    CargoEmpleadoCreateView,
    EmpleadoListView,
    EmpleadoCreateView,
    PerfilEmpleadoFormView,
)

urlpatterns = [
    url(r'^$', PerfilEmpleadoFormView.as_view(), name='perfil'),
    url(r'^crear/$', EmpleadoCreateView.as_view(), name='crear'),
    url(r'^listar/$', EmpleadoListView.as_view(), name='listar'),
    url(r'^habilidad/$', HabilidadCreateView.as_view(), name='habilidad'),
    url(r'^cargo/$', CargoEmpleadoCreateView.as_view(), name='cargo'),
]
