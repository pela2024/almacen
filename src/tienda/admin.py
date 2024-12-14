from django.contrib import admin

# Register your models here.
from .models import Comision, Alumno, Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre")

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("comision", "dni")



@admin.register(Comision)
class ComisionAdmin(admin.ModelAdmin):
    list_display = ("curos", "numero", "fecha_de_inicio")