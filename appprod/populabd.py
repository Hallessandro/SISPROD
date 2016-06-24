from django.db import transaction,IntegrityError

from appprod.models import Cargo, Prestador_servico, Unidade_medida, Materia_prima, Etapa, EtapaMateria, \
    Processo_producao

cargo1 = Cargo(descricao='vendedor',salario=880)
cargo2 = Cargo(descricao='produtor',salario=1180)

cargo1.save()
cargo2.save()


prestator1 =  Prestador_servico(nome='joão',telefone='91223-4432',email='joa@gmail.com',dt_nasc='1997-01-01',cpf='00033422333',cargo=cargo1)
prestator2 =  Prestador_servico(nome='Monic',telefone='81223-4432',email='monic@gmail.com',dt_nasc='1993-06-30',cpf='10033422333',cargo=cargo1)
prestator3 =  Prestador_servico(nome='Juliana',telefone='92023-4432',email='juli@gmail.com',dt_nasc='1997-03-02',cpf='12033422333',cargo=cargo2)

prestator1.save()
prestator2.save()
prestator3.save()


unidade1 = Unidade_medida(sigla='kg',descricao='kilograma')
unidade2 = Unidade_medida(sigla='g',descricao='grama')
unidade3 = Unidade_medida(sigla='ml',descricao='miligrama')

unidade1.save()
unidade2.save()
unidade3.save()


materia1 = Materia_prima(descricao='banana',unidade=unidade1,quantidade=440,custo=200)
materia2 = Materia_prima(descricao='peixe',unidade=unidade1,quantidade=500,custo=200)
materia3 = Materia_prima(descricao='milho',unidade=unidade1,quantidade=110,custo=200)
materia4 = Materia_prima(descricao='doce de goiaba',unidade=unidade2,quantidade=230,custo=200)

materia1.save()
materia2.save()
materia3.save()
materia4.save()


etapa1=Etapa(descricao='Avaliando estoque de produtos')
etapa2=Etapa(descricao='preparando produtos')
etapa3=Etapa(descricao='produtos pronto')


etapa1.save()
etapa2.save()
etapa3.save()


etapamateria1 = EtapaMateria(etapa=etapa1,materia=materia1,qtdUsada=10)
etapamateria2 = EtapaMateria(etapa=etapa1,materia=materia2,qtdUsada=20)
etapamateria3 = EtapaMateria(etapa=etapa1,materia=materia1,qtdUsada=12)
etapamateria4 = EtapaMateria(etapa=etapa2,materia=materia3,qtdUsada=20)
etapamateria5 = EtapaMateria(etapa=etapa2,materia=materia3,qtdUsada=29)
etapamateria6 = EtapaMateria(etapa=etapa2,materia=materia4,qtdUsada=30)

etapamateria1.save()
etapamateria2.save()
etapamateria3.save()
etapamateria4.save()
etapamateria5.save()
etapamateria6.save()

processo1 = Processo_producao(dt_inicio='2016-01-01',dt_fim='2016-01-20',descricao='pronto para consumo',etapas=etapa3)
processo2 = Processo_producao(dt_inicio='2016-02-01',dt_fim='2016-02-20',descricao='pronto para consumo',etapas=etapa3)
processo3 = Processo_producao(dt_inicio='2016-02-01',dt_fim='2016-02-10',descricao='pronto para consumo',etapas=etapa3)

prestator1.save()
prestator2.save()
prestator3.save()