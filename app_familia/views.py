from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from app_familia.models import Familia

# Create your views here.

def lista_familia(request):
    queryset = Familia.objects.all()
    diccionario = {'app_familia': queryset}
    plantilla = loader.get_template('templates1.html')
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)