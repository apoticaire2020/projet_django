from django.http import HttpResponse
import datetime
from django.template import Template , Context

class persona(object):
    def __init__(self , nom , appe) :
        self.nombre = nom
        self.appelido = appe


def saludo(request):
     
    p1 = persona("ahmed " , "fares")
    #nombre = "ahmed aboudrar"
    #appelido = "naqa"
    ahora=  datetime.datetime.now()
    doc_externo = open('C:/Users/hp/OneDrive/demo/django/Proyecto1/Proyecto1/plantillas/miplantilla.html')
    
    plt = Template(doc_externo.read())

    doc_externo.close()
    tem= ['plantillas' , 'vistas','formularios', 'modelos','database']

    ctx = Context({'nombre_persona':p1.nombre , 'smiya':p1.appelido , 'saaa':ahora , 'temas':tem })

    documento = plt.render(ctx)

    return HttpResponse(documento)

def byby(request):
    return HttpResponse("by alumnos ")

def damefecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h1>
    fecha y hora actual %s
    </h1>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento) 

def calculEdad(request ,edad, agno):
    #edad_actual = 52
    periodo=agno - 2021
    edadFutura = edad + periodo
    documento = "<html><body><h1> en  el agno %s tendras %s anos " %(agno,edadFutura) 
    return HttpResponse(documento) 
