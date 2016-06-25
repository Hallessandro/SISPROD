from django.shortcuts import render
from django.http import HttpResponse
from appprod.models import *


def home(request):
    return render(request,'base.html')

def exibirPrestador(request):
        prestador = Prestador_servico.objects.all().order_by('nome')
        return render(request,'exibirprestador.html', {'prestador':prestador})

def exibirMateria(request):
        materia = Materia_prima.objects.all().order_by('descricao')
        return render(request,'exibirMateriaPrima.html', {'materia':materia})

def exibirProcesso(request):
    processo = Processo_producao.objects.all().order_by('descricao')
    return render(request, 'exibirProcessoProducao.html', {'processo': processo})