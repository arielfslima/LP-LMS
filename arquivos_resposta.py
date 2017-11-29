from aluno import *
from questao import *

class Arquivos_Resposta(Aluno,Questao):

    def __init__(self):
        self.nome_disciplina = self.nome
        self.ano_ofertado = self.ano
        self.semestre_ofertado = self.semestre
        self.id_turma = self.id
        self.numero_questao = self.numero
        self.ra_aluno = self.ra
        self.arquivo = None

    '''Característica 38 - Resumo das entregas pendentes (professor).'''

    def entregas_pendentes(self):
        lista_concluido = []
        lista_pendente = []
        for i in lista_pendente:
            lista_pendente.append(self.ra_aluno)
            if self.arquivo == True:
                lista_pendente.remove(self.ra_aluno)
                lista_concluido.append(self.ra_aluno)

        return (lista_pendente)

    '''Característica 37 - Resumo das entregas ecebidas (professor)'''

    def entregas_concluidas(self):
        lista_concluido = []
        lista_pendente = []
        for i in lista_pendente:
            lista_pendente.append(self.ra_aluno)
            if self.arquivo == True:
                lista_pendente.remove(self.ra_aluno)
                lista_concluido.append(self.ra_aluno)

        return (lista_concluido)