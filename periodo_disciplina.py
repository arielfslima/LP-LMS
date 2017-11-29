from curso import *
from periodo import *
from grade_curricular import *
from disciplina import *
class Periodo_Disciplina(Curso,Periodo,Grade_Curricular,Disciplina):
    def __init__(self):
        self.sigla_curso = self.sigla
        self.ano_grade = self.ano
        self.semestre_grade = self.semestre
        self.numero_periodo = self.numero
        self.nome_disciplina = self.nome
