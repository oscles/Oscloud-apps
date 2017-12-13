from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import FormEvento
from .models import Evento


class EventoCreateView(LoginRequiredMixin, CreateView):
    form_class = FormEvento
    template_name = 'admin_oscloud/eventos/calendario_eventos.html'
    success_url = reverse_lazy('evento:crear')


class EventoListView(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'admin_oscloud/eventos/listar.html'
    context_object_name = 'listado_eventos'
    ordering = 'nombre'
