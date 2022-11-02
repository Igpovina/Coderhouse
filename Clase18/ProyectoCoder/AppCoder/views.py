import re
from django.shortcuts import redirect, render
from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import  DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def curso(request, nombre, camada):
    
    curso = Curso(nombre = nombre , camada = camada)
    curso.save()
    return HttpResponse(f"""
                        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado! </p>
                        """) 

@login_required    
def lista_curso(request):
    
    lista = Curso.objects.all()
    
    return render(request, 'lista_cursos.html', {"lista_cursos": lista})
        
def inicio(request):
    return render(request, 'inicio.html')

@login_required
def vista_curso(request):
    lista = Curso.objects.all()
    
    return render(request, 'cursos.html', {"lista_cursos": lista})
    

def profesores(request):
    return render(request, 'profesores.html')

def alumno(request):
    return render(request, 'alumno.html')

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

def leer_profesores(request):
    profesores = Profesor.objects.all()
    contexto = {'profesores':profesores}
    return render(request, 'profesores.html', contexto)

def crear_profesor(request):
    if request.method == 'POST':
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            profesor = Profesor(nombre = data['nombre'], apellido = data['apellido'], e_mail = data['e_mail'], profesion = data['profesion'])
            profesor.save()
            return redirect('leer_profesores')
        
    else:
        mi_formulario = ProfesorFormulario()
            
        return render(request, 'profesorFormulario.html', {'mi_formulario':mi_formulario})
    
def eliminar_profesor(request, id):
    if request.method == 'POST':
        data = request.POST
        profesor = Profesor.objects.get(id = id)
        profesor.delete()
        
        profesores = Profesor.objects.all()
        return render(request, 'profesores.html', {'profesores':profesores})
    
    
def editar_profesor(request, id):
    
    profesor = Profesor.objects.get(id = id)
    if request.method == 'POST':
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            
            profesor.nombre = data['nombre']
            profesor.apellido = data['apellido']
            profesor.e_mail = data['e_mail']
            profesor.profesion = data['profesion']
            profesor.save()
            return redirect('leer_profesores')
        
    else:
        mi_formulario = ProfesorFormulario(initial={
            'nombre':profesor.nombre,
            'apellido':profesor.apellido,
            'e_mail':profesor.e_mail,
            'profesion':profesor.profesion,
        })
            
        return render(request, 'editarProfesor.html', {'mi_formulario':mi_formulario, 'id':profesor.id})
 
    
class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'curso_list.html'
    

class CursoDetail(DetailView):
    model = Curso
    template_name = 'curso_detail.html'
    

class CursoCreate(CreateView):
    model = Curso
    template_name = 'curso_create.html'
    fields = ['nombre', 'camada']
    success_url = '/AppCoder/' 
    
    
class CursoUpdate(UpdateView):
    model = Curso
    template_name = 'curso_update.html'
    fields = ('__all__')
    success_url= '/AppCoder/'
    

class CursoList(ListView):
    model = Curso
    template_name = 'curso_detail.html'
    
    
def login_user(request):
    if request.method == 'POST':
        mi_formulario = AuthenticationForm(request, data=request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            usuario = data['username']
            pwd = data['password']
            
            user = authenticate(username = usuario, password = pwd)
            
            if user:
                login(request, user)
                return render(request, 'inicio.html', {'mensaje':f'bienvenido {usuario}'})
            else:
                return render(request, 'inicio.html', {'mensaje':f'usuario invalido'})
        return render(request, 'inicio.html', {'mensaje':f'formulario invalido'})
        
    else:
        mi_formulario = AuthenticationForm()
            
        return render(request, 'login.html', {'mi_formulario':mi_formulario})



def register_user(request):
    if request.method == 'POST':
        mi_formulario = UserCreationForm(request.POST)
        if mi_formulario.is_valid():
            username = mi_formulario.cleaned_data['username']
            mi_formulario.save()
            
            return render(request, 'inicio.html', {'mensaje':f'Usuario {username} creado'})
        else:
            
            return render(request, 'inicio.html', {'mensaje':f'Error al crear el usuario'})
        
    else:
        mi_formulario = UserCreationForm()
            
        return render(request, 'register.html', {'mi_formulario':mi_formulario})

