from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView


from .. forms import LiquidacionForm
from .. models import Liquidacion

class  LiquidacionListView(ListView):
    model = Liquidacion

class LiquidacionCreateView(CreateView):
    model= Liquidacion
    form_class = LiquidacionForm
    success_url = reverse_lazy ("tienda:liquidacion_list")     

class LiquidacionUpdateView(UpdateView):
    model= Liquidacion
    form_class = LiquidacionForm
    success_url = reverse_lazy ("tienda:liquidacion_list")      

class LiquidacionDetailView(DetailView):
    model= Liquidacion
    success_url = reverse_lazy ("liquidacion:liquidacion_list")        