import re
from django.shortcuts import redirect, render
from .models import Curso
from .forms import CursoFormulario
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
    

def profesores(request):
    return render(request, 'profesores.html')
    \

def alumno(request):
    return render(request, 'alumno.html')
    return HttpResponse('vista alumno')

def entregable(request):
    return render(request, 'entregables.html')
    
def cursoFormulario(request):
    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            curso = Curso(nombre = data['curso'], camada = data['camada'])
            curso.save()
            return redirect('Cursos')
        
    else:
        mi_formulario = CursoFormulario()
            
        return render(request, 'cursoFormulario.html', {'mi_formulario':mi_formulario})

def busqueda_cadama(request):
    return render(request, 'busquedaCamada.html')

def buscar(request):
    camada = request.GET['camada']
    cursos = Curso.objects.get(camada = camada)
    return render(request, 'buscar.html', {'cursos':cursos})