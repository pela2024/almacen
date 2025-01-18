from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from tienda.models import  Consorcio, Liquidacion
from tienda.forms import  LiquidacionForm




class  LiquidacionListView(ListView):
    model = Liquidacion


class LiquidacionCreateView(CreateView):
    model = Liquidacion
    fields = ['periodo', 'consorcio']  # Ajusta los campos según tu modelo
    template_name = 'liquidacion_form.html'

    def get_initial(self):
        # Captura el consorcio_id desde la URL
        consorcio_id = self.kwargs.get('consorcio_id')
        consorcio = get_object_or_404(Consorcio, pk=consorcio_id)
        
        # Retorna los valores iniciales para el formulario
        return {'consorcio': consorcio}

    def form_valid(self, form):
        # Asigna el consorcio automáticamente antes de guardar
        consorcio_id = self.kwargs.get('consorcio_id')
        form.instance.consorcio = get_object_or_404(Consorcio, pk=consorcio_id)
        return super().form_valid(form)
  

class LiquidacionUpdateView(UpdateView):
    model= Liquidacion
    form_class = LiquidacionForm
    success_url = reverse_lazy ("tienda:liquidacion_list")      

class LiquidacionDetailView(DetailView):
    model= Liquidacion
    success_url = reverse_lazy ("liquidacion:liquidacion_list")        