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
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    
class Profesor(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    e_mail= models.EmailField()
    profesion = models.CharField(max_length = 30)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Entregable(models.Model):
    nombre = models.CharField(max_length = 30)
    nota = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre}'