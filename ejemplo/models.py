from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    fecha = models.DateField(default=True)
    
def __str__(self):
    return f"{self.nombre}, {self.numero_pasaporte}, {self.id},  {self.direccion}, {self.fecha}"