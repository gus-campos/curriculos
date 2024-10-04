from enum import Enum
class Tipo(Enum):
    obrigatoria = 0
    eletiva1 = 1
    eletiva2 = 2
    optativa = 3
    tcc = 5

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.__repr__()
    

class Curso:
    def __init__(self, dict=None, tipo=None, feito=False):

        """
        Inicializa atributos de acordo com valores do dicionário.
        """

        # Pegando valores do dicionário
        self.nome = self.get("NOME", dict).upper()
        self.codigo = self.get("CÓDIGO", dict)
        self.nota = self.get("NOTA", dict)
        self.ch = self.get("CH", dict)
        self.reqs = self.get("REQ", dict)
        self.eqvs = self.get("EQV", dict)

        self.tipo = tipo
        self.possivel = False
        self.feito = feito

        # Separando requisto em lista, e tirandos as letras "e"
        if self.reqs is not None:
            self.reqs = self.reqs.split()
            self.reqs = ([item.replace(",","") for item 
                          in self.reqs if item not in ["e","ou"] ])
        else:
            self.reqs = []

        # Separando requisto em lista, e tirandos as letras "e"
        if self.eqvs is not None:
            self.eqvs = self.eqvs.split()
            self.eqvs = ([item.replace(",","") for item 
                          in self.reqs if item not in ["e","ou"] ])
        else:
            self.eqvs = []

    # ========================= Impressão =====================================

    def __repr__(self):
        """ Define representação do objeto """
        return f"{self.codigo} | {self.nome}"
    
    def __str__(self):
        """ 
        Determina que quando o objeto for convertido em string (quando 
        for impresso), será usada a sua representação. 
        """
        return self.__repr__()

    # ========================= Auxiliar ======================================

    def correspondente(self, curric):
        """Retorna a disciplina de outro currículo que correponde a este"""
        return curric.busca(self.codigo)

    @staticmethod
    def get(value, dict):
        """ Pega um valor do dicionário, se houver """
        if value in dict.keys():
            return dict[value]
        else:
            return
        
# =============================================================================

class Curriculo:
    def __init__(self, cursos=None, tipo=None, feito=False):
        self.cursos = cursos
        self.ch = {

            Tipo.obrigatoria : 0,
            Tipo.eletiva1 : 0,
            Tipo.eletiva2 : 0
        }

        # Passando tipos, sem sobrescrever 
        for curso in self.cursos:
            curso.tipo = tipo if curso.tipo is None else curso.tipo

        # Passando feito, sem sobrescrever 
        for curso in self.cursos:
            curso.feito = feito if curso.feito is None else curso.feito

    # ============================= Auxiliar ==================================

    def codigos(self):
        """Retorna a lista de todos os códigos dos cursos deste curriculo"""

        codigos = []
        for curso in self.cursos:
            codigos.append(curso.codigo)
        return codigos
    
    def busca(self, codigos):
        """
        Retorna uma lista de cursos correspondentes a uma lista de códigos. 
        Se for passada uma string, devolve uma disciplina apenas.
        """

        # Transformando código punico em lista unitária
        if not isinstance(codigos, list):
            codigos = [codigos]

        # Listando disciplinas 
        cursos = []
        for curso in self.cursos:
            if curso.codigo in codigos:
                cursos.append(curso)
        
        # Se for passado mais de um código, só aceitar resultados perfeitos
        if len(cursos) > 1 and len(cursos) != len(codigos):
            raise AssertionError("Número inconsistentes de cursos encontrados")

        # Decidindo forma de retorno
        if len(codigos) == 1:
            return None if len(cursos) == 0 else cursos[0]
        else:
            return cursos

    # ============================ Atualização ================================

    def atualiza_feito(self, hist):
        """
        Atualiza o atributo 'feito' de todos os cursos do currículo, de 
        acordo com um histórico.
        """

        for curso in self.cursos:    
            if curso.codigo in hist.codigos():
                curso.feito = True

    def atualiza_possivel(self, hist):
        """
        Atualiza o atributo 'possivel' de todos os cursos do currículo, de 
        acordo com um histórico.
        """

        for curso in self.cursos:    

            if len(curso.reqs) == 0:
                curso.possivel = True

            else:
                reqs_satisfeitos = []
                for req in curso.reqs:
                    reqs_satisfeitos.append(req in hist.codigos())
                curso.possivel =  all(reqs_satisfeitos)

    def atualiza_ch(self):

        """ 
        Atualiza a carga horária do currículo de acordo com a soma da
        carga horária dos cursos.
        """

        for curso in self.cursos:
            if curso.feito:
                self.ch[curso.tipo] += curso.ch

    def atualiza(self, hist):

        """
        Realiza todas as atualizações.
        """

        self.atualiza_feito(hist)
        self.atualiza_possivel(hist)
        self.atualiza_ch()

    # ====================== Funcionalidades ==================================

    def em_comum(self, curric):
        """Retorna cursos em comum entre este e outro currículo"""
        
        # Achando códigos em comum
        codigos_em_comum = list(set(self.codigos())
                                .intersection(curric.codigos()))

        # Retornando disciplinas em comum
        return self.busca(codigos_em_comum)
    
    def ira(self):
        """ Calcula o IRA """
        soma_notas = 0
        soma_ch = 0
        for curso in self.cursos:
            soma_notas += curso.nota * curso.ch
            soma_ch += curso.ch
        return round(soma_notas/soma_ch, 2)

    def append(self, cursos):
        self.cursos.append(cursos)
        return cursos

    @staticmethod
    def from_csv(path, map=lambda x:x, tipo=None, feito=False):
        """ Cria um currículo a partir de um CSV """
        import pandas as pd
        import numpy as np

        table = pd.read_csv(path)
        cursos = []
        for item in table.replace(np.nan, None).map(map).iloc:
            cursos.append(Curso(item.to_dict(), tipo=tipo, feito=feito))
        return Curriculo(cursos)
            
# =============================================================================
