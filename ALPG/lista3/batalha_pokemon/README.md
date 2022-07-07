# Batalha Pokemon

## Descrição

Serra e seus amigos estavam jogando pokemon no seu gameboy color antes de uma monitoria de matemática discreta que um dos seus amigos ia ministrar. Como todos devem conhecer, pokemon é um jogo onde as batalhas são baseadas em turnos, onde, em cada turno, o pokemon mais rápido pode usar sua habilidade primeiro. Cada pokemon tem uma quantidade inteira de vida V e um dano inicial inteiro D. A batalha termina quando um dos pokemons perde toda sua vida. Como Serra e seus amigos não são muito bons nesses novos jogos de pokemon, seus pokemons principais possuem apenas duas habilidades, um ataque de dano, que se escolhido causa um dano D igual ao dano atual do pokemon no seu adversário, e outra habilidade especial que se escolhida aumenta permanentemente o seu dano em 50 unidades. Um de seus amigos, Bezaliel, disse para Serra que ele deveria sempre usar o ataque de dano, visto que a outra habilidade era “inútil”. Já seu outro amigo, Clodes, usando como base seus conhecimentos em matemática discreta, falou que ocasionalmente usar a habilidade especial do seu pokemon pode ser a diferença entre ganhar ou perder uma batalha. Depois de muita discussão sobre qual era a melhor estratégia, Clodes e Bezaliel decidiram resolver suas diferenças em uma batalha pokemon onde cada treinador deveria se manter fiel a sua estratégia (Bezaliel vai atacar todos os turnos até derrotar o inimigo ou perder tentando, enquanto Clodes vai usar a habilidade de incrementar o dano de seu pokemon até chegar num ponto que não possa mais perder e só então começar a atacar).

.Em um turno, um pokemon pode usar APENAS UMA de suas habilidades.

.Considere que o pokemon de Clodes é o mais rápido, ou seja, ele sempre ataca primeiro.

.Considere que cada treinador joga de maneiro ótima, se mantendo sempre fiel a sua estratégia.

Formato de entrada

No início você receberá um numero  1 <= n <= 1000, o numero de batalhas a serem disputadas (considere que cada batalha é independente).

Em seguida, você receberá n linhas contendo quarto números inteiros cada, V1, V2, D1 e D2, onde V1 é a vida do pokemon de Clodes e D1 seu dano inicial. V2 e D2 são a vida e dano inicial do pokemon de Bezaliel, respectivamente.

. 1 <=V1, V2, D1, D2 <= 1000000


## Formato de saída

Para cada batalha, sua resposta deve ser uma única linha contendo “Clodes” ou “Bezaliel”, sem aspas, o nome do treinador que deverá ganhar aquela batalha.

## Exemplos de:
________________________________________________________________
### Entrada

    3
    100 500 20 50
    1000 1000 20 30
    10000 10500 10 50

### Saída

    Bezaliel
    Clodes
    Clodes
________________________________________________________________

[Ver no The Huxley](https://thehuxley.com/problem/1250?quizId=7373)