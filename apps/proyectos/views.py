# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.mixins import ContextDataMixin
from .forms import FormTecnologia, FormProyectos, FormTipoProyecto
from .models import Tecnologia, TipoProyecto, Proyecto


class TecnologiaCreateView(ContextDataMixin, LoginRequiredMixin, CreateView):
    context_object_name = 'listado_tecnologias'
    model = Tecnologia
    form_class = FormTecnologia
    template_name = 'admin_oscloud/proyectos/crear_tecnologia.html'
    success_url = reverse_lazy('proyecto:tecnologia')


class TipoProyectoCreateView(ContextDataMixin, LoginRequiredMixin, CreateView):
    context_object_name = 'listado_tipo_proyectos'
    model = TipoProyecto
    form_class = FormTipoProyecto
    template_name = 'admin_oscloud/proyectos/crear_categoria.html'
    success_url = reverse_lazy('proyecto:categoria')


class ProyectoCreateView(LoginRequiredMixin, CreateView):
    form_class = FormProyectos
    template_name = 'admin_oscloud/proyectos/crear.html'
    success_url = reverse_lazy('proyecto:listar')


class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'admin_oscloud/proyectos/listar.html'
    context_object_name = 'listado_proyectos'
    ordering = '-id'
