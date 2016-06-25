from appprod.models import Processo_producao, Prestador_servico

'''Liste os processos produtivos cadastrados, indicando os prestadores de
serviços vinculados, etapas envolvidas e itens de matéria prima utilizados,
apresentando ainda o custo total do processo, que é dado pelo seguinte
procedimento: Para cada Matéria Prima utilizada, calcule o subtotal, que é a
quantidade utilizada X o custo de aquisição. O somatório desse subtotais
gera o valor total. (Valor 1,0)'''

for ps in Processo_producao.objects.all():
    to= 0
    for e in ps.etapas.etapamateria_set.all():
        print(ps.descricao + ' etapa ' + ps.etapas.descricao)
        print((e.materia.custo*e.qtdUsada))



