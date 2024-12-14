from django import forms

from .models import Curso, Comision, Alumno

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__" 

class ComisionForm(forms.ModelForm):
    class Meta:
        model = Comision
        fields = "__all__"         

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = "__all__"           