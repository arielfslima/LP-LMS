class Disciplina:

    def __init__(self):
        self.nome = ''
        self.carga_horaria = None
        self.teoria = None
        self.pratica = None
        self.ementa = ''
        self.competencias = ''
        self.habilidades = ''
        self.conteudo = ''
        self.bibliografia_basica = ''
        self.bibliografia_complementar = ''
        self.p1 = None
        self.t1 = None
        self.p2 = None
        self.t2 = None

    '''Característica 1 - Consulta de boletim.'''

    def media_disciplina(self):
        mb1 = ((self.p1 * 0.7) + (self.t1 * 0.3))
        mb2 = ((self.p2 * 0.7) + (self.t2 * 0.3))
        media_final = (mb1 + mb2) / 2
        return 'Sua média semestral em',self.nome,'é de:',media_final

    '''Característica 16 - Confirmação de matrícula'''

    def calssificacao_matricula(self):
        matriculados = []
        if matricula == True:
            media_final = float(input('Digite a média de suas notas: '))
            ordem = int(input('Digite seu número de matricula: '))
            while media > 8 or matricula < 60:
                matriculados.append(matricula)
            while media > 6 and media <= 8 or matricula >= 60 and matricula < 80:
                matriculados.append(matricula)
            while media <= 6 or matricula >= 80:
                matriculados.append(matricula)
                break
