"""
Módulo que a partir dos objetos já criados pelo módulo read, analisa 
quais as próximas disciplinas que poderei fazer.
"""

from classes import Tipo
from read import cc, ce, hist

# =============================================================================

print("\n", "="*10, "OBRIGATÓRIAS - PERÍODO 2","="*10, "\n")

# Atualizando cursos feitos, de acordo com o histórico
ce.atualiza(hist)
cc.atualiza(hist)

# Para cada curso de Ciências Exatas
for curso in ce.cursos:

    # Achar o curso correspondente no currículo de Ciência da Computação    
    corresp = curso.correspondente(cc)

    # Se o correspondente existir, for obrigatório, 
    # eu tiver os requisitos, e ainda não tiver sido feito
    if (corresp is not None 
        and corresp.tipo == Tipo.obrigatoria
        and curso.possivel
        and not curso.feito):
            
            # Imprimir o curso, e marcar como concluído, 
            # para simulação do período seguinte
            print(curso)
            curso.feito = True
            hist.append(curso)

# Inserção manual por quebra de pré-requisito ultrapassado
hist.append(ce.busca("DCC107"))
print(hist.append(ce.busca("DCC025")))

# =============================================================================

ce.atualiza(hist)

print("\n", "="*10, "OBRIGATÓRIAS - PERÍODO 3","="*10, "\n")

for curso in ce.cursos:
    corresp = curso.correspondente(cc)

    if (corresp is not None 
        and corresp.tipo == Tipo.obrigatoria
        and curso.possivel
        and not curso.feito):
            
            print(curso)
            curso.feito = True

ce.atualiza(hist)