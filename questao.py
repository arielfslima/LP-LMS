from turma import *
from disciplina_ofertada import *
from disciplina import *
class Questao(Turma,Disciplina_Ofertada,Disciplina):

    def __init__(self):
        self.nome_disciplina = self.nome
        self.ano_ofertado = self.ano
        self.semestre_ofertado = self.semestre
        self.id_turma = self.id
        self.numero = None
        self.data_limite_entrega = None
        self.descricao = ''
        self.data = None

