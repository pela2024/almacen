from django.contrib import admin

# Register your models here.
from .models import Comision, Alumno, Consorcio

@admin.register(Consorcio)
class ConsorcioAdmin(admin.ModelAdmin):
    list_display = ("domicilio",)

    

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ("Comision", "Dni")



@admin.register(Comision)
class ComisionAdmin(admin.ModelAdmin):
    list_display = ("Consorcio__domicilio", "Numero", "Fecha_de_inicio")
