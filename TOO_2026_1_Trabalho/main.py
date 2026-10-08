from model.heroi import Heroi
from model.missao import MissaoCaca, MissaoEscolta, MissaoExploracao
from model.enums import ClasseHeroi

def main():
    heroi = Heroi('Francisco', ClasseHeroi.GUERREIRO, 100, 100, 20, 10)
    missoes = [
        MissaoCaca('Caça aos goblins', 'Derrotar cinco goblins', 100, 5),
        MissaoEscolta('Carruagem segura', 'Escoltar três viajantes', 100, 3),
        MissaoExploracao('Ruínas antigas', 'Explorar quatro locais', 100, 4),
    ]

    print('Tentativa de concluir uma missão pendente:')
    try:
        missoes[0].concluir_missao(heroi)
    except ValueError as erro:
        print(f'Erro tratado: {erro}')

    for missao in missoes:
        print(f'\n--- {missao.nome} ---')
        print('Herói antes da missão:')
        print(heroi.exibir_dados())
        print(missao)
        print(f'Recompensa pendente: {missao.calcular_recompensa()} XP')

        print(missao.iniciar_missao())
        print(missao)
        print(f'Recompensa em andamento: {missao.calcular_recompensa()} XP')

        missao.concluir_missao(heroi)
        print(missao)
        print(f'Recompensa entregue: {missao.calcular_recompensa()} XP')
        print('Herói depois da missão:')
        print(heroi.exibir_dados())


if __name__ == '__main__':
    main()
