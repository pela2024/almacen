from django.http import HttpRequest , HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from tienda.models import Consorcio
from tienda.forms import ConsorcioForm
from django.shortcuts import  get_object_or_404
from tienda.utils import verificar_consorcio


### CONSORCIO - LIST VIEW 

def consorcio_list(request):
    consorcios = Consorcio.objects.all()
    return render(request, 'tienda/consorcios_list.html', {'object_list': consorcios})


@verificar_consorcio
def detalle_consorcio(request, pk):
    consorcio = get_object_or_404(Consorcio, pk=pk)
    # Verificar si el usuario pertenece al consorcio
    if request.user.consorcio != consorcio:
        return HttpResponseForbidden("No tienes permiso para acceder a este consorcio.")
    liquidaciones = consorcio.liquidacion_set.all()
    ultima_liquidacion = liquidaciones.last() if liquidaciones.exists() else None
   
    return render(request, 'tienda/detalle_consorcio.html', {
        'consorcio': consorcio,
        'liquidaciones': liquidaciones,
        'ultima_liquidacion': ultima_liquidacion
    })


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