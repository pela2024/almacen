from django import forms
from .models import Consorcio, Liquidacion, Unidades, Propietario, Usuario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Proveedor
from .models import Gastos


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model= AuthenticationForm
        fields = ["username", " password"]

class CustomRegistroUsuarioForm(UserCreationForm):
    clave_del_consorcio = forms.CharField(max_length=255, required=True, label="Clave del Consorcio")

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'clave_del_consorcio', 'password1', 'password2']

    def clean_clave_del_consorcio(self):
        clave = self.cleaned_data.get("clave_del_consorcio")
        try:
            consorcio = Consorcio.objects.get(clave_del_consorcio=clave)
        except Consorcio.DoesNotExist:
            raise forms.ValidationError("La clave del consorcio no es válida.")
        return consorcio

    def save(self, commit=True):
        user = super().save(commit=False)
        user.consorcio = self.cleaned_data.get("clave_del_consorcio")
        if commit:
            user.save()
        return user

class ConsorcioForm(forms.ModelForm):
    class Meta:
        model = Consorcio
        fields = "__all__" 

class LiquidacionForm(forms.ModelForm):
    class Meta:
        model = Liquidacion
        fields = "__all__"         

class UnidadesForm(forms.ModelForm):
    class Meta:
        model = Unidades
        fields = "__all__"           


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name'] 

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Guardar el email del usuario
        if commit:
            user.save()
        return user          

class PropietarioRegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=255)
    apellido = forms.CharField(max_length=255)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    unidad = forms.ModelChoiceField(queryset=Unidades.objects.all())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'nombre', 'apellido', 'email', 'telefono', 'unidad')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Propietario.objects.create(
                user=user,
                unidad=self.cleaned_data['unidad'],
                nombre=self.cleaned_data['nombre'],
                apellido=self.cleaned_data['apellido'],
                email=self.cleaned_data['email'],
                telefono=self.cleaned_data['telefono']
            )
        return user
    

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['razon_social', 'cuit', 'actividad', "rubro"]


class GastosForm(forms.ModelForm):
    class Meta:
        model = Gastos
        fields = [ 'comprobante', 'concepto', 'a', 'importe']
        widgets = {
            'comprobante': forms.TextInput(attrs={'class': 'form-control'}),
            'concepto': forms.TextInput(attrs={'class': 'form-control'}),
            'a': forms.TextInput(attrs={'class': 'form-control'}),
            'importe': forms.NumberInput(attrs={'class': 'form-control'}),
        }
