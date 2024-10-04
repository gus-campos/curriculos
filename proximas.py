"""
Módulo que a partir dos objetos já criados pelo módulo read, analisa 
quais as próximas disciplinas que poderei fazer.
"""

from classes import Tipo
from read import cc, ce, hist

# =============================================================================

print("\n", "="*10, "OBRIGATÓRIAS - PERÍODO 2","="*10, "\n")

for curso in ce.cursos:
    
    corresp = curso.correspondente(cc)

    if (corresp is not None 
        and corresp.tipo == Tipo.obrigatoria
        and curso.possivel
        and not curso.feito):
            print(curso)
            curso.feito = True
            hist.append(curso)

hist.append(ce.busca("DCC107"))
print(hist.append(ce.busca("DCC025")), "\b*")

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