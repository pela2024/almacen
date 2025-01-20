from django.http import HttpRequest , HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from tienda.models import Consorcio
from tienda.forms import ConsorcioForm
from django.shortcuts import  get_object_or_404
from functools import wraps


### CONSORCIO - LIST VIEW 

def consorcio_list(request):
    consorcios = Consorcio.objects.all()
    return render(request, 'tienda/consorcios_list.html', {'object_list': consorcios})


def verificar_consorcio(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        consorcio_id = kwargs.get('pk')
        consorcio = get_object_or_404(Consorcio, pk=consorcio_id)
        if request.user.consorcio != consorcio:
            return HttpResponseForbidden("No tienes permiso para acceder a este consorcio.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view


#### CONSORCIO - CREATE VIEW 
def consorcio_create(request: HttpRequest)-> HttpResponse:
    if request.method =="GET":
        form = ConsorcioForm()
    if request.method == "POST":
        form = ConsorcioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:consorcio_list")   
    return render(request, "tienda/consorcio_form.html", {"form": form})    



#### CONSORCIO - UPDATE VIEWS 
def consorcio_update(request: HttpRequest, pk:int)-> HttpResponse:
   query = Consorcio.objects.get(id=pk)
   if request.method =="GET":
        form = ConsorcioForm(instance =query) 
   if request.method == "POST":
        form = ConsorcioForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("tienda:consorcio_list")   
   return render(request, "tienda/consorcio_form.html", {"form": form})

 #### CONSORCIO DETAIL VIEWS
def consorcio_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # Obtener el consorcio actual
    consorcio_actual = get_object_or_404(Consorcio, id=pk)
    
    # Obtener todos los demás consorcios excepto el actual
    otros_consorcios = Consorcio.objects.exclude(id=pk)
    
    # Pasar ambos al contexto
    return render(request, "tienda/consorcio_detail.html", {
        "object": consorcio_actual,         # Consorcio actual
        "otros_consorcios": otros_consorcios,  # Otros consorcios
    })
   #### CONSORCIO DELETE VIEWS
def consorcio_delete(request: HttpRequest, pk:int)-> HttpResponse:
   query = Consorcio.objects.get(id=pk)
   if request.method == "POST" :
        query.delete()
        return redirect ("tienda:consorcio_list")
   return render(request, "tienda/consorcio_confirm_delete.html", {"object": query})