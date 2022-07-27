from django.db import models

# Create your models here.
class Estudiante(models.Model):
    codigo = models.IntegerField()
    dni = models.IntegerField()
    nombre = models.CharField(max_length=150)
    apepat = models.CharField(max_length=150)
    apemat = models.CharField(max_length=150)
    direccion = models.CharField(max_length=300)
    telefono = models.IntegerField()
    estado = models.CharField(max_length=30)
