from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required  # type = ignore
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView 

from .forms import CustomAuthenticationForm , CustomRegistroUsuarioForm, UserProfileForm, UnidadesForm
from .models import Unidades 
# Create your views here.
@login_not_required 
def index(request):
    return render(request, "tienda/index.html")

@login_not_required
def about(request):
    return render(request, "tienda/about.html")

class CustomLoginView(LoginView): 
    authentication_form = CustomAuthenticationForm
    template_name = "tienda/login.html"

    def get_success_url(self):
        role = self.request.POST.get('role', '')
        
        if role == 'propietario' and hasattr(self.request.user, 'propietario'):
            return reverse_lazy('tienda:propietario_index')
        elif role == 'usuario' or not hasattr(self.request.user, 'propietario'):
            return reverse_lazy('tienda:index')
        elif self.request.user.is_staff:
            return reverse_lazy('admin:index')
        
        # Default fallback
        return reverse_lazy('tienda:index')

    def form_valid(self, form):
        usuario = form.get_user()
        role = self.request.POST.get('role', '')
        
        if role == 'propietario' and not hasattr(usuario, 'propietario'):
            messages.error(self.request, "No tienes permisos de propietario")
            return self.form_invalid(form)
            
        messages.success(
            self.request, f"Inicio de sesión exitoso. ¡Bienvenido {usuario.username}!"
        )
        return super().form_valid(form)

@method_decorator(login_not_required, name = "dispatch")
class RegistrarseView(CreateView):
    form_class = CustomRegistroUsuarioForm  # Usa el formulario personalizado
    template_name = 'tienda/register.html'  # Nombre del template
    success_url = reverse_lazy('tienda:login')  # Redirige al login tras el registro

    def form_valid(self, form:BaseModelForm) -> HttpResponse:
        messages.success(self.request, "Registro exitoso. Ahora puedes iniciar sesion ")
        return super().form_valid(form) 

class UpdateProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'tienda/profile.html'  # Nombre del template
    success_url = reverse_lazy('tienda:index') 

    def get_object (self):

        return self.request.user


def Unidades_list(request):
    query = Unidades.objects.all()
    context = {"object_list": query}
    return render(request, "tienda/unidades_list.html", context)

def Unidades_create(request):
    if request.method == "GET":
        form = UnidadesForm()
    elif request.method == "POST":
        form = UnidadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:unidades_list")
    return render(request, "tienda/unidades_form.html", {"form": form})     