# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 01:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição do cargo')),
                ('salario', models.FloatField(verbose_name='Salário')),
            ],
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição da etapa')),
            ],
        ),
        migrations.CreateModel(
            name='EtapaMateria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtdUsada', models.IntegerField(verbose_name='Quantidade de materia usada')),
                ('etapa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appprod.Etapa')),
            ],
        ),
        migrations.CreateModel(
            name='Materia_prima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição do produto')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade em estoque')),
                ('custo', models.FloatField(verbose_name='Preço de aquisição')),
            ],
        ),
        migrations.CreateModel(
            name='Prestador_servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=10, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('dt_nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appprod.Cargo', verbose_name='Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Processo_producao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inicio', models.DateField(verbose_name='Data de inicio')),
                ('dt_fim', models.DateField(verbose_name='Data de término')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição do processo')),
                ('etapas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appprod.Etapa')),
                ('prestadores', models.ManyToManyField(to='appprod.Prestador_servico')),
            ],
        ),
        migrations.CreateModel(
            name='Unidade_medida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=2, verbose_name='Sigla')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
            ],
        ),
        migrations.AddField(
            model_name='materia_prima',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appprod.Unidade_medida', verbose_name='Unidade de medida'),
        ),
        migrations.AddField(
            model_name='etapamateria',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appprod.Materia_prima'),
        ),
        migrations.AddField(
            model_name='etapa',
            name='materia',
            field=models.ManyToManyField(through='appprod.EtapaMateria', to='appprod.Materia_prima'),
        ),
    ]
