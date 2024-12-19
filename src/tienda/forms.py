from django import forms

from .models import Consorcio, Liquidacion, Unidades

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