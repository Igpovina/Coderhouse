from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.
def curso(request, nombre, camada):
    
    curso = Curso(nombre = nombre , camada = camada)
    curso.save()
    return HttpResponse(f"""
                        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado! </p>
                        """) 
    
def lista_curso(request):
    
    lista = Curso.objects.all()
    
    return render(request, 'lista_cursos.html', {"lista_cursos": lista})
        
def inicio(request):
    return render(request, 'inicio.html')
    return HttpResponse('vista inicio')

def vista_curso(request):
    lista = Curso.objects.all()
    
    return render(request, 'cursos.html', {"lista_cursos": lista})
    # return render(request, 'cursos.html')
    # return HttpResponse('vista cursos')

def profesores(request):
    return render(request, 'profesores.html')
    return HttpResponse('vista profesores')

def alumno(request):
    return render(request, 'alumno.html')
    return HttpResponse('vista alumno')

def entregable(request):
    return render(request, 'entregables.html')
    return HttpResponse('vista entregable')