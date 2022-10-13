from asyncore import read
from http.cookiejar import LoadError
from django.http import HttpResponse
from datetime import datetime as dt
from django.template import Template, Context, loader
from django.shortcuts import render

def saluda(request):
    return HttpResponse('Holis :)')

def segunda_vista(request):
    return HttpResponse("""
                        <h1>Bienvenido a mi primer pag web</h1>
                        <br>
                        <br>
                        <p>Esto es muy loco </p>
                        """)
    
def dia_de_hoy(request):
    dia = dt.now()
    documento_texto = f'hoy es : <br>{dia}'
    return HttpResponse(documento_texto)

def saluda_con_nombre(request, nombre):
    
    documento_texto = f'Mi nombre es: {nombre}'
    return HttpResponse(documento_texto)

def probando_template(request):
    # mi_HTML = open(r"C:\\Users\nacho\OneDrive\Documentos\GitHub\Coderhouse\Clase17\project\project\templates\templates1.html")
    diccionario = {'my_name':'Ignacio'}
    plantilla = loader.get_template('templates1.html')
    # plantilla = Template(mi_HTML.read())
    
    # mi_HTML.close()
    
    # mi_contexto = Context({'my_name':'Ignacio'})
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)