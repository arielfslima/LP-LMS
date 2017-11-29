'''Imports'''
from aluno import Aluno
from curso import Curso
from disciplina import Disciplina
from arquivos_resposta import *
from arquivos_questao import Arquivos_Questao
'''Definindo valores'''
aluno1 = Aluno()
aluno1.nome = 'Gabriel'
aluno1.ra = '1700727'
curso1 = Curso()
curso1.sigla = 'SI'
disciplina1 = Disciplina()
disciplina1.nome = 'LP'
disciplina1.p1 = 10
disciplina1.t1 = 10
disciplina1.p2 = 10
disciplina1.t2 = 10
arquivoresposta1 = Arquivos_Resposta()
arquivoquestao1 = Arquivos_Questao()
'''Teste Funçao 1'''
print('Teste 1:')
disciplina1.media_disciplina()
print(disciplina1.media_disciplina())

'''Teste Funçao 2'''
print('Teste 2:')
aluno1.aplicacao_teste()
print(aluno1.aplicacao_teste())

'''Teste Funçao 3'''
print('Teste 3:')
arquivoresposta1.entregas_concluidas()
print(arquivoresposta1.entregas_concluidas())

'''Teste Funçao 4'''
print('Teste 4:')
arquivoresposta1.entregas_pendentes()
print(arquivoresposta1.entregas_pendentes())

'''Teste Funçao 5'''
print('Teste 5:')
arquivoquestao1.prazo()
print(arquivoquestao1.prazo())

'''Teste Funçao 6'''
print('Teste 6:')
aluno1.matricula_on()
print(aluno1.matricula_on())

'''Teste Funçao 7'''
print('Teste 7:')
aluno1.max_matriculas()
print(aluno1.max_matriculas())

'''Teste Funçao 8'''
print('Teste 8:')
