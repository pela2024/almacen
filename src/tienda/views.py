from django.http import HttpRequest , HttpResponse
from django.shortcuts import redirect, render

from .models import Consorcio, Unidades, Liquidacion
from .forms import ConsorcioForm, LiquidacionForm, UnidadesForm
# Create your views here.
def index(request):
    return render(request, "tienda/index.html")

def about(request):
    return render(request, "tienda/about.html")

#### CONSORCIO - LIST VIEW 
def consorcio_list(request:HttpRequest)-> HttpResponse:
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




def Liquidacion_list(request):
    query = Liquidacion.objects.all()
    context ={"object_list": query}
    return render(request, "tienda/Liquidacion_list.html", context)

def Liquidacion_create(request):
    if request.method =="GET":
        form = LiquidacionForm()
    if request.method == "POST":
        form = LiquidacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:liquidacion_list")   
    return render(request, "tienda/liquidacion_form.html", {"form": form})  

def Unidades_list(request):
    query = Unidades.objects.all()
    context ={"object_list": query}
    return render(request, "tienda/unidades_list.html", context)

def Unidades_create(request):
    if request.method =="GET":
        form = UnidadesForm()
    if request.method == "POST":
        form = UnidadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:unidades_list")   
    return render(request, "tienda/unidades_form.html", {"form": form})  