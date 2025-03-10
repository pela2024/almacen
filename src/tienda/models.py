from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MinValueValidator

class Administracion(models.Model):
    razon_social = models.CharField(max_length=255, verbose_name="Razón Social")
    cuit = models.CharField(max_length=11, verbose_name="CUIT", unique=True)
    domicilio = models.CharField(max_length=255, verbose_name="Domicilio")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)

    def __str__(self):
        return self.razon_social


class Consorcio(models.Model):
    clave_del_consorcio = models.CharField(max_length=255, verbose_name="Clave del Consorcio")
    cuit = models.CharField(max_length=11, verbose_name="CUIT", unique=True)
    domicilio = models.CharField(max_length=255, verbose_name="Domicilio")
    administracion = models.ForeignKey(
        Administracion, 
        on_delete=models.CASCADE, 
        related_name="consorcios"
    )

    def __str__(self):
        return self.clave_del_consorcio



class Usuario(AbstractUser):
    consorcio = models.ForeignKey(
        'Consorcio',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="usuarios"
    )
    groups = models.ManyToManyField(
        Group,
        related_name='usuario_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuario_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return f"{self.username} ({self.consorcio})"


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


class Proveedor(models.Model):
    razon_social = models.CharField(max_length=150, blank=True, null=True)  # Opcional
    cuit = models.CharField(max_length=11, unique=True)  # CUIT único
    rubro = models.CharField(max_length=100, blank=True, null=True)  # Opcional
    actividad = models.TextField(blank=True, null=True)  # Campo largo opcional
    domicilio = models.CharField(max_length=255, verbose_name="Domicilio")  # Campo agregado
    

    def __str__(self):
        return f"{self.razon_social} - {self.cuit}"

class Gastos(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='gastos', null=True)
    consorcio = models.ForeignKey(Consorcio, on_delete=models.CASCADE, related_name='gastos', null=True)
    comprobante = models.CharField(max_length=22)
    concepto = models.CharField(max_length=1000)
    a = models.CharField(max_length=150)
    importe = models.DecimalField(max_digits=8, decimal_places=2)
    rubro = models.IntegerField()  # Este sería el campo de rubro

    class Meta:
        verbose_name = 'gasto'
        verbose_name_plural = 'gastos'
        

    def __str__(self):
        return f"{self.consorcio} - {self.proveedor} - {self.concepto}"
