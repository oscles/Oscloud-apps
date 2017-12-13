# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView

from apps.mixins import ContextDataMixin
from .forms import FormSkill, FormCargoEmpleado, FormEmpleado
from .models import Skill, CargoEmpleado, Empleado


class HabilidadCreateView(ContextDataMixin, LoginRequiredMixin, CreateView):
    context_object_name = 'listado_habilidades'
    template_name = 'admin_oscloud/empleados/crear_habilidad.html'
    form_class = FormSkill
    model = Skill
    success_url = reverse_lazy('empleado:habilidad')


class CargoEmpleadoCreateView(ContextDataMixin, LoginRequiredMixin, CreateView):
    context_object_name = 'listado_cargos'
    template_name = 'admin_oscloud/empleados/crear_cargo_empleado.html'
    form_class = FormCargoEmpleado
    model = CargoEmpleado
    success_url = reverse_lazy('empleado:cargo')


class EmpleadoCreateView(LoginRequiredMixin, CreateView):
    form_class = FormEmpleado
    template_name = 'admin_oscloud/empleados/crear.html'
    success_url = reverse_lazy('empleado:listar')


class EmpleadoListView(LoginRequiredMixin, ListView):
    model = Empleado
    context_object_name = 'listado_empleados'
    template_name = 'admin_oscloud/empleados/listar.html'
    ordering = 'first_name'


class PerfilEmpleadoFormView(ContextDataMixin, LoginRequiredMixin, FormView):
    form_class = FormEmpleado
    template_name = 'admin_oscloud/empleados/perfil.html'
    context_object_name = 'user'

    def get_queryset(self):
        return Empleado.objects.get(user_ptr_id=self.request.user.id)



