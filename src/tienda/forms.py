from django import forms
from .models import Consorcio, Liquidacion, Unidades
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustonAuthenticationForm(AuthenticationForm):
    class Meta:
        model= AuthenticationForm
        fields = ["username", " password"]

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields = ["username", "email" ," password1", "password2"]







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