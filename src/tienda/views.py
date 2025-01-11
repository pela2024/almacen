from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required  # type = ignore
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView 
from django.contrib.auth.decorators import login_required
from django.shortcuts import  get_object_or_404
from .models import Proveedor
from .forms import ProveedorForm



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
        # Redirige según el tipo de usuario
        if self.request.user.is_superuser:  # Administrador
            return reverse_lazy('admin:index')  # Cambia según tu URL de admin
        elif hasattr(self.request.user, 'propietario'):  # Usuario Propietario
            return reverse_lazy('tienda:propietario_index')  # Cambia según tu URL de propietario
        else:  # Usuario estándar
            return reverse_lazy('tienda:index')  # URL de usuario general

    def form_valid(self, form):
        # Mensaje de éxito al iniciar sesión
        messages.success(
            self.request, f"Inicio de sesión exitoso. ¡Bienvenido {self.request.user.username}!"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        # Mensaje de error si fallan las credenciales
        messages.error(self.request, "Usuario o contraseña incorrectos.")
        return super().form_invalid(form)

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

@login_required
def admin_dashboard_view(request):
    return render(request, "tienda/admin_dashboard.html")

@login_required
def propietario_dashboard_view(request):
    return render(request, "tienda/propietario_dashboard.html")


def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'tienda/proveedores/lista_proveedores.html', {'proveedores': proveedores})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proveedor creado exitosamente.")
            return redirect('tienda:lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'tienda/crear_proveedor.html', {'form': form})

def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, "Proveedor actualizado exitosamente.")
            return redirect('tienda:lista_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'tienda/editar_proveedor.html', {'form': form, 'proveedor': proveedor})

def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        messages.success(request, "Proveedor eliminado exitosamente.")
        return redirect('tienda:lista_proveedores')
    return render(request, 'tienda/eliminar_proveedor.html', {'proveedor': proveedor})