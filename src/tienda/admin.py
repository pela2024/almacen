from django.contrib import admin

# Register your models here.
from .models import Comision, Alumno, Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre",)

    

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("Comision", "Dni")



@admin.register(Comision)
class ComisionAdmin(admin.ModelAdmin):
    list_display = ("Curso__nombre", "Numero", "Fecha_de_inicio")
