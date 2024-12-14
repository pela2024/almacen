from django.db import models

# Create your models here.
class  Curso(models.Model):
    nombre =models.CharField(max_length=255, unique=True)

class Comision(models.Model):
    Curso =models.ForeignKey(Curso, on_delete= models.SET_NULL, null=True)
    Numero = models.PositiveIntegerField()
    Fecha_de_inicio =models.DateField() 

class Alumno(models.Model):
    Comision =models.ForeignKey(Comision, on_delete= models.SET_NULL, null=True) 
    Dni = models.IntegerField()


    