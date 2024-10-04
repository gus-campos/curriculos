"""
Módulo que faz a leitura dos arquivos e chama os construtures dos 
objetos necessários de acordo.
"""


from classes import Curso, Curriculo, Tipo

map = lambda x: None if (x=="---" or x=="missing") else x

# Histórico
hist = Curriculo.from_csv("dados/HIST/HISTÓRICO.csv", map=map, feito=True)

# CE Obrigatórias
ce_obg = Curriculo.from_csv("dados/CE/CE-OBRIGATÓRIAS.csv", map=map, tipo=Tipo.obrigatoria)
ce_elet1 = Curriculo.from_csv("dados/CE/CE-ELETIVAS1.csv", map=map, tipo=Tipo.eletiva1)
ce_elet2 = Curriculo.from_csv("dados/CE/CE-ELETIVAS2.csv", map=map, tipo=Tipo.eletiva2)
ce = Curriculo(ce_obg.cursos + ce_elet1.cursos + ce_elet2.cursos)

# CC
cc_obg = Curriculo.from_csv("dados/CC/CC-OBRIGATÓRIAS.csv", map=map, tipo=Tipo.obrigatoria)
cc_elet = Curriculo.from_csv("dados/CC/CC-ELETIVAS.csv", map=map, tipo=Tipo.eletiva1)
cc_comp = Curriculo.from_csv("dados/CC/CC-ELETIVAS-COMP.csv", map=map, tipo=Tipo.eletiva2)
cc = Curriculo(cc_obg.cursos + cc_elet.cursos + cc_comp.cursos)