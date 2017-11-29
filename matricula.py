from aluno import *
from disciplina import *
from disciplina_ofertada import *
from turma import *
class Matricula(Aluno,Disciplina,Disciplina_Ofertada,Turma):

    def __init__(self):
        self.ra_aluno = self.ra
        self.nome_disciplina = ''
        self.ano_ofertado = self.ano
        self.semestre_ofertado = self.semestre
        self.id_turma = self.id