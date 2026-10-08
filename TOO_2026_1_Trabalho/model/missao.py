from model.enums import StatusMissao


class Missao:
    # Apenas o status possui setter, pois muda conforme a missão avança no jogo.
    # Nome, descrição e recompensa são definidos na criação e ficam só para leitura.

    def __init__(self, nome, descricao, recompensa):
        self.__nome = nome
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__status = StatusMissao.PENDENTE

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

    @status.setter
    def status(self, valor):
        if not isinstance(valor, StatusMissao):
            raise ValueError('Status inválido: use um valor do enum StatusMissao.')

        transicoes = {
            StatusMissao.PENDENTE: StatusMissao.EM_ANDAMENTO,
            StatusMissao.EM_ANDAMENTO: StatusMissao.CONCLUIDA
        }

        proximo_status = transicoes.get(self.__status)

        if valor is not proximo_status:
            raise ValueError(
                f'Transição inválida: {self.__status.name} -> {valor.name}. '
                'A sequência permitida é PENDENTE -> EM_ANDAMENTO -> CONCLUIDA.'
            )

        self.__status = valor

    def iniciar_missao(self):
        self.status = StatusMissao.EM_ANDAMENTO
        return f'A missão {self.nome} começou! O objetivo é {self.descricao}.'

    def exibir_dados(self):
        msg = f'''
[{self.__class__.__name__}]
Nome: {self.nome}
Descrição: {self.descricao}
Recompensa: {self.recompensa}
Status: {self.status.value}
'''
        return msg

    def __str__(self):
        return f'missão [{self.__class__.__name__}]: {self.nome} | status: {self.status.value}'
