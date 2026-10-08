from model.enums import StatusMissao


class Missao:
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

    # Apenas o status possui setter, pois muda conforme a missão avança no jogo.
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

    def calcular_recompensa(self):
        if self.status is not StatusMissao.CONCLUIDA:
            return 0
        return self.recompensa

    def concluir_missao(self, heroi):
        self.status = StatusMissao.CONCLUIDA
        heroi.ganhar_experiencia(self.calcular_recompensa())

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


class MissaoCaca(Missao):
    def __init__(self, nome, descricao, recompensa, quantidade_inimigos):
        super().__init__(nome, descricao, recompensa)
        self.__quantidade_inimigos = quantidade_inimigos

    @property
    def quantidade_inimigos(self):
        return self.__quantidade_inimigos

    def calcular_recompensa(self):
        recompensa_base = super().calcular_recompensa()
        if self.status is not StatusMissao.CONCLUIDA:
            return 0
        # Cada inimigo da missão acrescenta 10 XP à recompensa.
        return recompensa_base + self.quantidade_inimigos * 10


class MissaoEscolta(Missao):
    def __init__(self, nome, descricao, recompensa, quantidade_escoltados):
        super().__init__(nome, descricao, recompensa)
        self.__quantidade_escoltados = quantidade_escoltados

    @property
    def quantidade_escoltados(self):
        return self.__quantidade_escoltados

    def calcular_recompensa(self):
        recompensa_base = super().calcular_recompensa()
        if self.status is not StatusMissao.CONCLUIDA:
            return 0
        # Cada pessoa escoltada acrescenta 20 XP à recompensa.
        return recompensa_base + self.quantidade_escoltados * 20


class MissaoExploracao(Missao):
    def __init__(self, nome, descricao, recompensa, quantidade_locais):
        super().__init__(nome, descricao, recompensa)
        self.__quantidade_locais = quantidade_locais

    @property
    def quantidade_locais(self):
        return self.__quantidade_locais

    def calcular_recompensa(self):
        recompensa_base = super().calcular_recompensa()
        if self.status is not StatusMissao.CONCLUIDA:
            return 0
        # Cada local explorado acrescenta 15 XP à recompensa.
        return recompensa_base + self.quantidade_locais * 15
