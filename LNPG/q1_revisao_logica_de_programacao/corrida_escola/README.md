# A corrida da escola

Tempo máximo de execução: 1s

Tópicos: array, acumulador, decisão

## Descrição

A escola de Joãozinho tradicionalmente organiza uma corrida ao redor do prédio. Como todos os alunos são
convidados a participar e eles estudam em períodos diferentes, é difícil que todos corram ao mesmo tempo.

Para contornar esse problema, os professores cronometram o tempo que cada aluno demora para dar cada volta
ao redor da escola, e depois comparam os tempos para descobrir a classificação final.

Sua tarefa é, sabendo o número de competidores, o número de voltas de que consistiu a corrida e os tempos
de cada aluno competidor, descobrir quem foi o aluno vencedor, para que ele possa receber uma medalha
comemorativa.

## Formato de entrada

A primeira linha da entrada contém dois inteiros N e M representando o número de competidores e o número
de voltas da corrida, respectivamente.

Cada uma das N linhas seguintes representa um competidor: a primeira linha representa o primeiro competidor,
a segunda linha representa o segundo competidor, e assim por diante. Cada linha contém M inteiros
representando os tempos em cada volta da corrida: o primeiro inteiro é o tempo da primeira volta, o segundo
inteiro é o tempo da segunda volta, e assim por diante.

Garante-se que não houve dois competidores que gastaram o mesmo tempo para completar a corrida inteira.

Considere:

• 2 <= N <= 100
• 1 <= M <= 100
• 1 <= qualquer número da entrada que represente o tempo de uma volta <= 1000000

## Formato de saída

A saída consiste de um único inteiro, que corresponde ao número do competidor que ganhou a corrida.

## Exemplos de:

### Entrada

    2 3
    5 1 2
    7 2 5

### Saída

    1

[Ver no TheHuxley](https://thehuxley.com/problem/207?quizId=7901)