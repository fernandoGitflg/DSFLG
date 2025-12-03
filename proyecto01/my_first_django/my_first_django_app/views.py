from django.http import HttpResponse
from django.template import loader
from .models import Persona

def index(request):
    return HttpResponse('<h1>Holamundo</h1><a href="mi_primera_vista>Moverse"</a>')

def mi_primera_vista(request):
    template= loader.get_template('mi_primera_template.html')
    return HttpResponse(template.render())

def listar_personas(request):
    personas = Persona.objects.all().values()
    template=loader.get_template('listar_personas.html')
    context ={
        'personas': personas,
    }
    return HttpResponse(template.render(context,request))
