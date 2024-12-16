from django.shortcuts import redirect, render

from .models import Consorcio, Alumno, Comision
from .forms import ConsorcioForm, ComisionForm, AlumnoForm
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

def comision_list(request):
    query = Comision.objects.all()
    context ={"object_list": query}
    return render(request, "tienda/comision_list.html", context)

def Comision_create(request):
    if request.method =="GET":
        form = ComisionForm()
    if request.method == "POST":
        form = ComisionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:comision_list")   
    return render(request, "tienda/comision_form.html", {"form": form})  

def alumno_list(request):
    query = Alumno.objects.all()
    context ={"object_list": query}
    return render(request, "tienda/alumno_list.html", context)

def Alumno_create(request):
    if request.method =="GET":
        form = AlumnoForm()
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:alumno_list")   
    return render(request, "tienda/alumno_form.html", {"form": form})  