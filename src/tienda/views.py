from django.shortcuts import redirect, render

from .models import Consorcio, Unidades, Liquidacion
from .forms import ConsorcioForm, LiquidacionForm, UnidadesForm
# Create your views here.
def index(request):
    return render(request, "tienda/index.html")

def about(request):
    return render(request, "tienda/about.html")


def consorcio_list(request):
    query = Consorcio.objects.all()
    context ={"object_list": query}
    return render(request, "tienda/consorcio_list.html", context)

def consorcio_create(request):
    if request.method =="GET":
        form = ConsorcioForm()
    if request.method == "POST":
        form = ConsorcioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:consorcio_list")   
    return render(request, "tienda/consorcio_form.html", {"form": form})    

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