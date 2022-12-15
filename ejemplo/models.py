from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    fecha = models.DateField(default=True)
    
def __str__(self):
    return f"{self.nombre}, {self.numero_pasaporte}, {self.id},  {self.direccion}, {self.fecha}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=200)
    documento = models.IntegerField()
    
def __str__(self):
    return f"{self.nombre}, {self.puesto}, {self.id},  {self.documento}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    clase = models.CharField(max_length=200)
    nota_final = models.IntegerField()
    
def __str__(self):
    return f"{self.nombre}, {self.clase}, {self.id},  {self.nota_final}"
