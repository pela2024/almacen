from django.db import models





class Administracion(models.Model):
    razon_social = models.CharField(max_length=255, verbose_name="Razón Social")
    cuit = models.CharField(max_length=11, verbose_name="CUIT", unique=True)
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)

    def __str__(self):
        return self.razon_social