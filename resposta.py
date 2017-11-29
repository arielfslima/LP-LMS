from aluno import *
from disciplina import *
from disciplina_ofertada import *
from turma import *
from questao import *
class Resposta(Aluno,Disciplina,Disciplina_Ofertada,Turma,Questao):

    def __init__(self):
        self.nome_disciplina = self.nome
        self.ano_ofertado = self.ano
        self.semestre_ofertado = self.semestre
        self.id_turma = self.id
        self.numero_questao = self.numero
        self.ra_aluno = self.ra
        self.data_avaliacao = None
        self.nota = None
        self. avaliacao = ''
        self.descricao = ''
        self.data_de_envio = None