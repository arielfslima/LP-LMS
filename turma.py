from disciplina_ofertada import *
from professor import *
class Turma(Disciplina_Ofertada,Professor):
    def __init__(self):
        self.nome_disciplina = ''
        self.ano_ofertado = self.ano
        self.semestre_ofertado = self.semestre
        self.id = None
        self.turno = ''
        self.ra_professor = self.ra