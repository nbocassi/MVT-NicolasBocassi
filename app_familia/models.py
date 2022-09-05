from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre= models.CharField(max_length=128)
    apellido= models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    peso_kg = models.IntegerField()
    