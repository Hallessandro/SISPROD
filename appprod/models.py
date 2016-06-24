from django.db import models

# Create your models here.

class Cargo(models.Model):
    descricao = models.CharField("Descrição do cargo", max_length=150)
    salario = models.FloatField("Salário")

class Prestador_servico(models.Model):
    nome = models.CharField("Nome", max_length=150)
    telefone = models.CharField("Telefone", max_length=10)
    email = models.EmailField("Email")
    dt_nasc = models.DateField("Data de Nascimento")
    cpf = models.CharField("CPF", max_length=11)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, verbose_name="Cargo")

class Unidade_medida(models.Model):
    sigla = models.CharField("Sigla", max_length=2)
    descricao = models.CharField("Descrição", max_length=150)

class Materia_prima(models.Model):
    descricao = models.CharField("Descrição do produto", max_length=150)
    unidade = models.ForeignKey(Unidade_medida, on_delete=models.PROTECT, verbose_name="Unidade de medida")
    quantidade = models.IntegerField("Quantidade em estoque")
    custo = models.FloatField("Preço de aquisição")

class Etapa(models.Model):
    descricao = models.CharField("Descrição da etapa", max_length=150)
    materia = models.ManyToManyField(Materia_prima, through=EtapaMateria)

class EtapaMateria(models.Model):
    etapa = models.ForeignKey(Etapa, on_delete=models.PROTECT)
    materia = models.ForeignKey(Materia_prima, on_delete=models.PROTECT)
    qtdUsada = models.IntegerField("Quantidade de materia usada")

class Processo_producao(models.Model):
    dt_inicio = models.DateField("Data de inicio")
    dt_fim = models.DateField("Data de término")
    descricao = models.CharField("Descrição do processo", max_length=255)
    prestadores = models.ManyToManyField(Prestador_servico)
    etapas = models.ForeignKey(Etapa, on_delete=models.PROTECT)