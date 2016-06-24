from django.shortcuts import render
from django.http import HttpResponse
from appprod.models import *


def home(request):
    return render(request,'base.html')

def exibirPrestador(request,id):
        prestador = Prestador_servico.objects.order_by('nome')
        lista = {'prestador':prestador}
        return render(request, 'exibirprestador.html', {'prestador': prestador})






###########