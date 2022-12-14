"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from AppCoder.views import curso, lista_curso, inicio, vista_curso, profesores, alumno, register_user, entregable, cursoFormulario, busqueda_cadama, buscar, leer_profesores, crear_profesor,login_user, eliminar_profesor, editar_profesor,CursoList
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('agrega-curso/<nombre>/<camada>/', curso),
    path('ver-cursos/', lista_curso),
    path('', inicio, name='inicio'),
    path('vista-cursos/',vista_curso, name = 'Cursos'),
    path('profesores/', leer_profesores, name ='leer_profesores'),
    path('alumno/', alumno, name = 'Alumno' ),
    path('entregable/', entregable, name= 'Entregable'),
    path('cursoformulario/', cursoFormulario, name='cursoFormulario'),
    path('busqueda_camada/', busqueda_cadama, name='busqueda_camada'),
    path('buscar/', buscar, name='buscar'),
    path('crear-profesor/', crear_profesor, name='crear_profesores'),
    path('eliminar-profesor/<int:id>', eliminar_profesor, name='eliminar_profesor'),
    path('editar-profesor/<int:id>', editar_profesor, name='editar_profesor'),
    path('curso_list/', CursoList.as_view(), name='curso_list'),
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout')
]