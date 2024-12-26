from django.db import models


class Consorcio(models.Model):
    domicilio = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.domicilio


class Liquidacion(models.Model):
    consorcio = models.ForeignKey(Consorcio, on_delete=models.SET_NULL, null=True)
    periodo = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.consorcio} - {self.periodo}"


class Unidades(models.Model):
    liquidacion = models.ForeignKey(Liquidacion, on_delete=models.SET_NULL, null=True) 
    piso = models.IntegerField()
    depto = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.liquidacion} - Piso: {self.piso}, Depto: {self.depto}"
    class meta: 
        unique_together =("liquidacion", "piso")
        verbase_name =" unidad"
        verbase_name_pluraL="unidades"

