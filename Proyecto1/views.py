from django.http import HttpResponse
import datetime
from django.template import Template , Context




def saludo(request):
    doc_externo = open('C:/Users/hp/OneDrive/demo/django/Proyecto1/Proyecto1/plantillas/miplantilla.html')
    
    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context()

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
