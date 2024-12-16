from django.db import models

# Create your models here.
class  Consorcio(models.Model):
    domicilio =models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.domicilio


class Comision(models.Model):
    Consorcio =models.ForeignKey(Consorcio, on_delete= models.SET_NULL, null=True)
    Numero = models.PositiveIntegerField()
    Fecha_de_inicio =models.DateField() 
     
    def __str__(self):
        return  f"{self.Consorcio.domicilio} - {self.Numero}"

class Alumno(models.Model):
    Comision =models.ForeignKey(Comision, on_delete= models.SET_NULL, null=True) 
    Dni = models.IntegerField()


    