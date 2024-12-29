from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView 
from django.forms import BaseModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .forms import CustomAuthenticationForm , CustomRegistroUsuarioForm, UserProfileForm
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
    template_name = 'tienda/register.html'  # Nombre del template
    success_url = reverse_lazy('tienda:login')  # Redirige al login tras el registro


class UpdateProfileView(UpdateView):
    nmodel = User
    from_class = UserProfileForm
    template_name = 'tienda/profile.html'  # Nombre del template
    success_url = reverse_lazy('tienda:index') 

    def get_objetc (self):

        return self.request.user