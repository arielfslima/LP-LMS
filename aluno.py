from curso import *
class Aluno(Curso):

    def __init__(self):
        self.ra = None
        self.nome = ''
        self.email = ''
        self.celular = None
        self.sigla_curso = self.sigla

    '''Característica 15 - Matrículas online.'''

    def matricula_on(self):
        lista_matricula = []
        lista_matricula.append(self.nome)
        for self.nome in lista_matricula:
            if self.ra == True:
                print('Você já está matriculado RA:',self.ra)

    '''Característica 15 - Matrículas online.'''

    def max_matriculas(self):
        lista_matricula = []
        max = 60
        for i in lista_matricula:
            if len(lista_matricula) > max:
                print('Números de matriculados é maior que a quantidade máxima de alunos por turma.')

    '''Característica 3 - Aplicação de testes online.'''

    def aplicacao_teste(self):
        lista_teste = []
        for i in lista_teste:
            if self.ra not in lista_teste:
                lista_teste.append(self.ra)
        return lista_teste

