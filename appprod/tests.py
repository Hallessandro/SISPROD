from django.test import TestCase

# Create your tests here.

#SELECT pd.descricao,ps.nome,e.descricao,m.descricao,sum(custo*qtdUsada) FROM
 # appprod_prestador_servico ps INNER JOIN appprod_processo_producao_prestadores ppr
#on ps.id = ppr.prestador_servico_id INNER JOIN  appprod_processo_producao pd
#on pd.id = ppr.processo_producao_id INNER JOIN appprod_etapa e ON
#pd.etapas_id = e.id INNER JOIN appprod_etapamateria em ON
#e.id = em.etapa_id INNER JOIN appprod_materia_prima m ON em.materia_id = m.id