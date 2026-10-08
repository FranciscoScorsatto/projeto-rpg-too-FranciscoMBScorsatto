class Missao:

    def __init__(self, nome, descricao, recompensa):
        self.__nome = nome
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__status = 'PENDENTE'

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def recompensa(self):
        return self.__recompensa

    @property
    def status(self):
        return self.__status

    #Aletera durante o jogo, pois precisa mudar o valor para dar inicio.
    @status.setter
    def status(self, valor):
        if valor in ['PENDENTE', 'EM ANDAMENTO', 'CONCLUIDA']:
            self.__status = valor

    def iniciar_missao(self):
        if self.status == 'PENDENTE':
            self.status = 'EM ANDAMENTO'
            return f'A missão {self.nome} começou! O objetivo é {self.descricao}.'
        else:
            return f'A missão {self.nome} já foi iniciada!!!'

    def exibir_dados(self):
        msg = f'''
[{self.__class__.__name__}]
Nome: {self.nome}
Descrição: {self.descricao}
Recompensa: {self.recompensa}
Status: {self.status}
'''
        return msg

    def __str__(self):
        return f'missão [{self.__class__.__name__}]: {self.nome} | status: {self.status}'