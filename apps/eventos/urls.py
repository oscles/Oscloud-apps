from django.conf.urls import url

from .views import EventoCreateView, EventoListView

urlpatterns = [
    url(r'^$', EventoCreateView.as_view(), name='crear'),
    url(r'^listar/$', EventoListView.as_view(), name='listar'),
]