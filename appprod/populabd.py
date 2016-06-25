from django.db import transaction,IntegrityError

from appprod.models import Cargo, Prestador_servico, Unidade_medida, Materia_prima, Etapa, EtapaMateria, \
    Processo_producao

cargo1 = Cargo(descricao='Lorde Comandante',salario=880)
cargo2 = Cargo(descricao='Estagiário do Corvo de 3 olhos',salario=1180)
cargo3 = Cargo(descricao='Mão da Rainha Daenerys',salario=880)

cargo1.save()
cargo2.save()
cargo3.save()


prestator1 =  Prestador_servico(nome='Jon Snow',telefone='91223-4432',email='jon_knownothing@gmail.com',dt_nasc='1997-01-01',cpf='00033422333',cargo=cargo1)
prestator2 =  Prestador_servico(nome='Bran Stark',telefone='81223-4432',email='bran@gmail.com',dt_nasc='1993-06-30',cpf='10033422333',cargo=cargo2)
prestator3 =  Prestador_servico(nome='Tyrion Lannister',telefone='92023-4432',email='Tyrion@gmail.com',dt_nasc='1997-03-02',cpf='12033422333',cargo=cargo3)

prestator1.save()
prestator2.save()
prestator3.save()


unidade1 = Unidade_medida(sigla='KG',descricao='Kilograma')
unidade2 = Unidade_medida(sigla='G',descricao='Grama')
unidade3 = Unidade_medida(sigla='ML',descricao='Miligrama')

unidade1.save()
unidade2.save()
unidade3.save()


materia1 = Materia_prima(descricao='Banana',unidade=unidade1,quantidade=440,custo=200)
materia2 = Materia_prima(descricao='Peixe',unidade=unidade1,quantidade=500,custo=200)
materia3 = Materia_prima(descricao='Milho',unidade=unidade1,quantidade=110,custo=200)
materia4 = Materia_prima(descricao='Queijo',unidade=unidade2,quantidade=230,custo=200)

materia1.save()
materia2.save()
materia3.save()
materia4.save()


etapa1=Etapa(descricao='Avaliando estoque de produtos')
etapa2=Etapa(descricao='Preparando produtos')
etapa3=Etapa(descricao='Produtos pronto')


etapa1.save()
etapa2.save()
etapa3.save()


etapamateria1 = EtapaMateria(etapa=etapa1,materia=materia1,qtdUsada=8)
etapamateria2 = EtapaMateria(etapa=etapa1,materia=materia2,qtdUsada=5)
etapamateria3 = EtapaMateria(etapa=etapa1,materia=materia1,qtdUsada=12)
etapamateria4 = EtapaMateria(etapa=etapa2,materia=materia3,qtdUsada=10)
etapamateria5 = EtapaMateria(etapa=etapa2,materia=materia3,qtdUsada=9)
etapamateria6 = EtapaMateria(etapa=etapa2,materia=materia4,qtdUsada=8)

etapamateria1.save()
etapamateria2.save()
etapamateria3.save()
etapamateria4.save()
etapamateria5.save()
etapamateria6.save()

#inserção de processo
processo1 = Processo_producao(dt_inicio='2016-01-01',dt_fim='2016-01-20',descricao='Preparando monstros para sair da jaula',etapas=etapa3)
processo2 = Processo_producao(dt_inicio='2016-02-01',dt_fim='2016-02-20',descricao='Defendendo a muralha',etapas=etapa3)
processo3 = Processo_producao(dt_inicio='2016-02-01',dt_fim='2016-02-10',descricao='Ganhando preparo',etapas=etapa3)

processo1.save()
processo1.prestadores.add(prestator1, prestator2)
processo2.save()
processo2.prestadores.add(prestator3, prestator2)
processo3.save()
processo1.prestadores.add(prestator1, prestator3)