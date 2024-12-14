from django.shortcuts import redirect, render

from .models import Curso, Alumno, Comision
from .forms import CursoForm, ComisionForm, AlumnoForm
# Create your views here.
def index(request):
    return render(request, "tienda/index.html")

def about(request):
    return render(request, "tienda/about.html")


def curso_list(request):
    query = Curso.objects.all()
    context ={"object_list": query}
    return render(request, "tienda/curso_list.html", context)

def curso_create(request):
    if request.method =="GET":
        form = CursoForm()
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:curso_list")   
    return render(request, "tienda/curso_form.html", {"form": form})    

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
            return redirect("tienda:Comision_list")   
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
            return redirect("tienda:Alumno_list")   
    return render(request, "tienda/Alumno_form.html", {"form": form})  