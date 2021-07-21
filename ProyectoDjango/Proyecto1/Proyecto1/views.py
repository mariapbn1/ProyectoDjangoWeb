from django import http
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render


class Persona():

    def __init__(self, nombre, apellido, temas):
        self.nombre = nombre
        self.apellido = apellido
        self.temas = temas

def saludo(request): # Primera vista

    """
    Declarar variable
    nombre = 'Juan'
    apellido = 'Diaz'
    """
    fecha_actual = datetime.datetime.now()

    # Declarar instancia
    p1 = Persona('Juanito','Gutierrez',['Plantillas','Modelos','Formularios','Vistas','Despliegue de aplicación'])
    
    
    """
    Se agrega la dirección del documento
    doc_externo = open('/home/paulaberm/cursos/CursoDjango/ProyectoDjango/Proyecto1/Proyecto1/plantillas/miPlantilla.html')

    Creación de un objeto de tipo Template:
    plt = Template(doc_externo.read())

    Cerrar el documento
    doc_externo.close()
    

    ## Cargar elementos con LOADER
    doc_externo = get_template('miPlantilla.html')

    
    Crear contexto -> argumento que se pasa en el renderizado
    puede recibir diccionarios.
    ctx = Context({"nombre":p1.nombre, 'apellido':p1.apellido, 'fecha_actual':fecha_actual, 'temas':p1.temas})
    

    # Renderizar el documento.
    documento = doc_externo.render({"nombre":p1.nombre, 'apellido':p1.apellido, 'fecha_actual':fecha_actual, 'temas':p1.temas})
    """
    return render(request, 'miPlantilla.html', {"nombre":p1.nombre, 'apellido':p1.apellido, 'fecha_actual':fecha_actual, 'temas':p1.temas}) # Su objetivo es enviarnos esta respuesta

def despedida(request):

    return HttpResponse('Hasta luego alumnos de Django.')

# Ejemplo dinámico: Mostrar la fecha y hora actuales.
def dameFecha(request):

    fecha_actual = datetime.datetime.now()
    documento = '<html><body><h2>Fecha y hora actuales %s </h2></body></html>'% fecha_actual
    return HttpResponse(documento)

# Pasar parámetros en la url
def calcularEdad(request, edad, year):

    #edadActual = 18
    periodo = year - 2019
    edadFutura = edad + periodo
    documento = '<html><body><h2>En el año %s tendrás %s años </h2></body></html>' %(year, edadFutura) 
    return HttpResponse(documento)

def prueba(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'prueba.html', {'dameFecha':fecha_actual})
    

def prueba2(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'prueba2.html', {'dameFecha':fecha_actual})
    
    


    