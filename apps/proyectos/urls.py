from django.conf.urls import url

from .views import (
    ProyectoListView,
    ProyectoCreateView,
    TipoProyectoCreateView,
    TecnologiaCreateView
)

urlpatterns = [
    url(r'^$', ProyectoCreateView.as_view(), name='crear'),
    url(r'^listar/$', ProyectoListView.as_view(), name='listar'),
    url(r'^categoria/$', TipoProyectoCreateView.as_view(), name='categoria'),
    url(r'^tecnologia/$', TecnologiaCreateView.as_view(), name='tecnologia'),
]