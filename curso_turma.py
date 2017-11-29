from curso import *
from turma import *
from disciplina import *

class Curso_Turma(Curso, Turma):
    def __init__(self):
        self.sigla_curso = self.sigla
        self.nome_disciplina = self.nome
        self.ano_ofertado = self.ano 
        self.semestre_ofertado = self.semestre
        self.id_turma = self.id
