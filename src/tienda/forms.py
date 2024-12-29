from django import forms
from .models import Consorcio, Liquidacion, Unidades
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