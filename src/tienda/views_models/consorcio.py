from django.http import HttpRequest , HttpResponse
from django.shortcuts import redirect, render

from ..models import Consorcio
from ..forms import ConsorcioForm




### CONSORCIO - LIST VIEW 
def consorcio_list(request:HttpRequest)-> HttpResponse:
    busqueda = request.GET.get("busqueda", "")
    if busqueda:
       queryset = Consorcio.objects.filter(domicilio__icontains = busqueda)
    else: 
         queryset = Consorcio.objects.all()
    return render(request, "tienda/consorcio_list.html",{"object_list": queryset})

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
def consorcio_detail(request: HttpRequest, pk:int)-> HttpResponse:
   query = Consorcio.objects.get(id=pk)
   return render(request, "tienda/consorcio_detail.html", {"object": query})


   #### CONSORCIO DELETE VIEWS
def consorcio_delete(request: HttpRequest, pk:int)-> HttpResponse:
   query = Consorcio.objects.get(id=pk)
   if request.method == "POST" :
        query.delete()
        return redirect ("tienda:consorcio_list")
   return render(request, "tienda/consorcio_confirm_delete.html", {"object": query})