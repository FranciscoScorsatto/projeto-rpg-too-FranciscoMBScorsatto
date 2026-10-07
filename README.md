# Trabalho Avaliativo: Herança, Encapsulamento e Enum

**Disciplina:** Tecnologia de Orientação a Objetos  
**Valor:** 10,0 pontos  
**Pasta do projeto:** `TOO_2026_1_Trabalho/`

## Objetivo

Evoluir a classe `Missao` do RPG desenvolvido em aula, aplicando encapsulamento, enumeração de status e herança. Criar diferentes tipos de missão e integrar suas recompensas ao sistema de experiência do herói.

## O que já está pronto e deve ser preservado

- O herói já possui os atributos `nivel` e `xp` e o método `ganhar_experiencia()`.
- A classe `Personagem` já possui o método `_aumentar_atributos()`.
- **Não alterar esses métodos:** as missões devem utilizar a evolução já implementada.
- A regra de evolução é acumular **100 × nível atual de XP** para subir de nível: 100 XP do nível 1 ao 2, 200 XP do nível 2 ao 3 e assim por diante.
- O XP excedente permanece acumulado para o próximo nível.

## Parte 1 — Encapsulamento da classe Missao (1,5 ponto)

- [ ] Refatorar `Missao` seguindo o padrão adotado em `Personagem`.
- [ ] Tornar todos os atributos privados.
- [ ] Disponibilizar uma `@property` para leitura de cada atributo.
- [ ] Criar setters apenas para os atributos cuja alteração faça sentido durante o jogo.
- [ ] Justificar a escolha dos setters em um comentário no topo da classe.

## Parte 2 — Enum StatusMissao (2,0 pontos)

- [ ] Criar o enum `StatusMissao` com os valores `PENDENTE`, `EM_ANDAMENTO` e `CONCLUIDA`.
- [ ] Substituir o status em texto livre pelo enum.
- [ ] Garantir a sequência obrigatória: `PENDENTE → EM_ANDAMENTO → CONCLUIDA`.
- [ ] Impedir que etapas sejam puladas ou que o status retroceda.
- [ ] Gerar erros com mensagens claras para valores de status ou transições inválidas.

## Parte 3 — Três tipos de missão (4,5 pontos)

### Atributos próprios (2,5 pontos)

- [ ] Criar três subclasses de `Missao`.
- [ ] Definir pelo menos um atributo próprio em cada subclasse.
- [ ] Manter os atributos próprios privados e acessíveis por `property`.

Sugestões de tipos: caça, coleta, entrega, escolta ou exploração. Outros tipos também podem ser propostos.

### Cálculo de recompensa (2,0 pontos)

- [ ] Na classe mãe, fazer `calcular_recompensa()` retornar `0` quando o status não for `StatusMissao.CONCLUIDA` e retornar `self.recompensa` quando estiver concluída.
- [ ] Sobrescrever `calcular_recompensa()` nas três subclasses.
- [ ] Reaproveitar o cálculo da classe mãe usando `super()`.
- [ ] Somar um bônus derivado do atributo próprio de cada subclasse.
- [ ] Garantir que a recompensa total, incluindo o bônus, seja `0` enquanto a missão estiver pendente ou em andamento.

**Exemplo do enunciado:** uma missão de caça com recompensa base de 100 XP, cinco inimigos e bônus de 10 XP por inimigo deve retornar 150 XP quando concluída e 0 XP antes disso.

**Atenção:** uma subclasse que apenas muda um texto, sem atributo próprio nem sobrescrita do método, não atende ao requisito.

## Parte 4 — Entregar o XP ao herói (1,0 ponto)

- [ ] Implementar `concluir_missao(self, heroi)` na classe `Missao`.
- [ ] Alterar o status para `CONCLUIDA`, respeitando as regras de transição.
- [ ] Calcular a recompensa após a alteração do status, pois ela só é liberada depois da conclusão.
- [ ] Repassar a recompensa ao herói por meio do método existente `ganhar_experiencia()`.

## Parte 5 — Demonstração no main.py (1,0 ponto)

- [ ] Criar um herói.
- [ ] Criar uma missão de cada um dos três tipos.
- [ ] Colocar as missões em uma lista e percorrê-la chamando o mesmo método em todas, demonstrando polimorfismo.
- [ ] Executar o ciclo completo de uma missão: `PENDENTE → EM_ANDAMENTO → CONCLUIDA`.
- [ ] Demonstrar o herói subindo de nível com o XP recebido.
- [ ] Exibir os atributos do herói antes e depois da evolução.
- [ ] Provocar um erro de propósito, usando um status inválido ou uma transição proibida.
- [ ] Tratar o erro com `try/except` e exibir sua mensagem.

## Conferência final

- [ ] Conferir o encapsulamento da classe mãe e das subclasses.
- [ ] Conferir que transições inválidas geram erros claros.
- [ ] Conferir que nenhuma missão paga recompensa antes de ser concluída.
- [ ] Conferir que cada tipo de missão calcula seu bônus a partir do atributo próprio.
- [ ] Conferir que a conclusão entrega o XP ao herói e permite sua evolução.
- [ ] Conferir que os métodos de evolução fornecidos não foram alterados.
- [ ] Executar `main.py` e verificar todas as demonstrações exigidas.
