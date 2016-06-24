from django.shortcuts import render
from django.http import HttpResponse
from appprod.models import *


def home(request):
    return render(request,'base.html')

def exibirPrestador(request,id):
        prestador = Prestador_servico.objects.get(id=id)
        return render(request, 'exibirprestador.html', {'prestador': prestador})

