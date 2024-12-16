from django import forms

from .models import Consorcio, Comision, Alumno

class ConsorcioForm(forms.ModelForm):
    class Meta:
        model = Consorcio
        fields = "__all__" 

class ComisionForm(forms.ModelForm):
    class Meta:
        model = Comision
        fields = "__all__"         

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = "__all__"           