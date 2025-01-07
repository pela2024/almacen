from django import forms
from .models import Consorcio, Liquidacion, Unidades, Propietario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model= AuthenticationForm
        fields = ["username", " password"]


class CustomRegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Campo de email obligatorio

    class Meta:
        model = User  # Usamos el modelo de usuario predeterminado de Django
        fields = ['username', 'email', 'password1', 'password2']  # Campos necesarios

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Guardar el email del usuario
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