from grade_curricular import *
from curso import *
class Periodo(Grade_Curricular,Curso):
    def __init__(self):
        self.sigla_curso = self.sigla
        self.ano_grade = self.ano
        self.semestre_grade = self.semestre
        self.numero = None