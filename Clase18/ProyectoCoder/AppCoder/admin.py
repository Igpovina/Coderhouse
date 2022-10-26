import site
from django.contrib import admin
from .models import Curso,Alumno,Profesor,Entregable
# Register your models here.
admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Entregable)