from django.conf.urls import url

from .views import ClienteListView, ClienteCreateView

urlpatterns = [
    url(r'^$', ClienteCreateView.as_view(), name='crear'),
    url(r'^listar/$', ClienteListView.as_view(), name='listar'),
]
