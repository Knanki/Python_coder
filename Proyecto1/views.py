from django.http import HttpResponse
import datetime
from datetime import date
from django.template import Template, Context
from django.template import loader 

def saludo(request):   #Nuestra primera vista :) 
	return HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")

def diaDeHoy(request):

        dia = datetime.datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"


        return HttpResponse(documentoDeTexto)

def tercera_vista(request, fecha):
    fecha_actual = date.today()

    anio = fecha_actual.year
    
    fecha = int(fecha)

    resultado = anio - fecha
    
    retorno = f"El año en que naciste es : {resultado}"
    return HttpResponse(retorno)

def miNombreEs(self, nombre):

      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre}"


      return HttpResponse(documentoDeTexto)


def probandoTemplate(self):
    nom = "Gary"
    ap = "Aguilera"
    lista_notas = [2,2,3,7,2,5]
    dicc = {"nombre": nom, "apellido": ap, "hoy": datetime.datetime.now(), "notas": lista_notas}
    miHtml = open("C:/Users/garun/Desktop/ProyectoCoder/Proyecto1/plantillas/template1.html")
    plantilla = Template(miHtml.read())  
    miHtml.close()
    miContexto = Context(dicc)
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)