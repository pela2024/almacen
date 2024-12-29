from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView 
from django.forms import BaseModelForm
from django.contrib.auth.forms import AuthenticationForm

from .models import  Unidades
from .forms import   UnidadesForm
from .forms import CustomAuthenticationForm , CustomRegistroUsuarioForm
# Create your views here.
def index(request):
    return render(request, "tienda/index.html")

def about(request):
    return render(request, "tienda/about.html")

class CustomLoginView(LoginView): 
    authenticationform = CustomAuthenticationForm
    template_name = "tienda/login.html"
    next_page = reverse_lazy("tienda:index")

    def form_valid(self, form: AuthenticationForm)-> HttpResponse:
        usuario = form.get_user()
        messages.success (
            self.request, f"Inicio de secion exitoso !Bienvenido {usuario.username}"
        )
        return super().form_valid(form)


class RegistrarseView(CreateView):
    form_class = CustomRegistroUsuarioForm  # Usa el formulario personalizado
    template_name = 'register.html'  # Nombre del template
    success_url = reverse_lazy('login')  # Redirige al login tras el registro

    




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