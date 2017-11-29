from questao import *
'''Importando a biblioteca de datas.'''
from datetime import date
class Arquivos_Questao(Questao):

    def __init__(self):
        self.nome = self.nome
        self.ano = self.ano
        self.semestre = self.semestre
        self.id = self.id
        self.numero = self.numero
        self.aquivo = ''

    '''Caracteísticas 36 - Fechamento de entregas vencido o prazo.'''

    def prazo(self):
        hoje = date.today()
        entrega = date.fromordinal(hoje.toordinal() + 14)
        if hoje > entrega:
            print('Prazo de entregas vencido.')
