from django.shortcuts import render
from django.http import HttpResponse
from appprod.models import*


def home(request):
    return render(request,'base.html')

def exibirPrestador(request):
        prestador = Prestador_servico.objects.all()
        return render(request, 'exibirprestador.html', {'prestador': prestador})


def exibirMateriaPrima(request, descricao):
    materia = Materia_prima.objects.get(descricao=descricao)
    return render(request, 'exibirMateria.html', {'materia': materia})

