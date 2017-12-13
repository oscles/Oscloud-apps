from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import FormCliente
from .models import Cliente


class ClienteCreateView(LoginRequiredMixin, CreateView):
    form_class = FormCliente
    template_name = 'admin_oscloud/clientes/crear.html'
    success_url = reverse_lazy('cliente:listar')


class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    context_object_name = 'listado_clientes'
    template_name = 'admin_oscloud/clientes/listar.html'
    ordering = 'nombre'