from django.db import models

# Create your models here.
# clases que django transforma en tablas
class Curso(models.Model):
    
    nombre = models.CharField(max_length = 30)
    camada = models.IntegerField()
    
class Alumno(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    e_mail= models.EmailField()