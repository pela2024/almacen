from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from ..models import Liquidacion, Propietario
from ..forms import PropietarioRegistroForm

class PropietarioRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return hasattr(self.request.user, 'propietario')

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        raise PermissionDenied("No tienes permisos de propietario.")

class PropietarioIndexView(PropietarioRequiredMixin, TemplateView):
    template_name = 'tienda/propietario/index.html'

class LiquidacionesPropietarioListView(PropietarioRequiredMixin, ListView):
    model = Liquidacion
    template_name = 'tienda/propietario/liquidaciones_list.html'
    context_object_name = 'liquidaciones'

    def get_queryset(self):
        try:
            propietario = self.request.user.propietario
            consorcio = propietario.consorcio
            if consorcio:
                return Liquidacion.objects.filter(consorcio=consorcio).order_by('-periodo')
            return Liquidacion.objects.none()
        except (AttributeError, Propietario.DoesNotExist):
            return Liquidacion.objects.none()

class LiquidacionPropietarioDetailView(PropietarioRequiredMixin, DetailView):
    model = Liquidacion
    template_name = 'tienda/propietario/liquidacion_detail.html'
    context_object_name = 'liquidacion'

    def test_func(self):
        try:
            propietario = self.request.user.propietario
            liquidacion = self.get_object()
            return propietario.consorcio == liquidacion.consorcio
        except (AttributeError, Propietario.DoesNotExist):
            return False

class PropietarioRegistroView(CreateView):
    form_class = PropietarioRegistroForm
    template_name = 'tienda/propietario/registro.html'
    success_url = reverse_lazy('tienda:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
