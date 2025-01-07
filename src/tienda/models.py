from django.db import models
from django.contrib.auth.models import User

class Consorcio(models.Model):
    clave_del_consorcio = models.CharField(max_length=255, default="valor_default")
    domicilio = models.CharField(max_length=255)
    localidad =models.CharField(max_length=255, default = "caba")
    provincia = models.CharField(max_length=255, default ="Buenos Aires")
    cuit = models.CharField(max_length=11)

    def __str__(self):
        return self.domicilio

class Liquidacion(models.Model):
    consorcio = models.ForeignKey(Consorcio, on_delete=models.SET_NULL, null=True)
    periodo = models.CharField(max_length=255)

    class Meta:
        unique_together = ('consorcio', 'periodo')  # Restricción única compuesta

    def __str__(self):
        return f"{self.consorcio}"



class Unidades(models.Model):
    liquidacion = models.ForeignKey(Liquidacion, on_delete=models.SET_NULL, null=True) 
    piso = models.IntegerField()
    depto = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.liquidacion} - Piso: {self.piso}, Depto: {self.depto}"
    class Meta: 
        unique_together =("liquidacion", "piso")
        verbose_name ="unidad"
        verbose_name_plural="unidades"


class Propietario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidades, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.unidad}"

    @property
    def consorcio(self):
        return self.unidad.liquidacion.consorcio if self.unidad else None
