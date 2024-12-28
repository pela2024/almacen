from django.contrib import admin

# Register your models here.
from .models import Liquidacion, Unidades , Consorcio


@admin.register(Consorcio)
class ConsorcioAdmin(admin.ModelAdmin):
    list_display = ("domicilio",)

@admin.register(Unidades)
class UnidadesAdmin(admin.ModelAdmin):
    list_display = ("liquidacion","piso","depto",)
    list_display_links=("piso",)
    list_filter=("liquidacion",)
    list_fields=("liquidacion",)

@admin.register(Liquidacion)
class LiquidacionAdmin(admin.ModelAdmin):
    list_display = ("consorcio","periodo", )


