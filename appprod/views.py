from django.shortcuts import render
from django.http import HttpResponse
from appprod.models import *


def home(request):
    return render(request,'base.html')

def exibirPrestador(request,id):
        prestador = Prestador_sevico.objects.get(id=id)
        return render(request, 'exibirprestador.html', {'prestador': prestador})

