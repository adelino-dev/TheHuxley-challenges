# 5 maiores do sorteio

_Tempo máximo de execução: 1s_

_Tópicos: ordenação_

## Descrição

Dado um quantidade de números N,  um dígito sorteado D e N números, sua tarefa é informar os 5 maiores números sorteados que possuem o ultimo dígito igual a D, caso não exista números suficientes você deve substitui-los por -1.

Os números devem ser impressos em ordem crescente.

## Formato de entrada

Dois inteiros N e D, seguidos de N números não negativos.

5 <= N <= 1000.

0 <= D <= 9.

## Formato de saída

Os 5 maiores números sorteados , 1 por linha, ou -1 quando necessário.

## Exemplos de:


### Entrada

    10 3
    2
    3
    13
    51
    21
    31
    11
    2
    3
    5

### Saída

    -1
    -1
    3
    3
    13

_____________________________________

### Entrada

    10 1
    2
    3
    11
    51
    21
    31
    11
    2
    3
    5

### Saída

    11
    11
    21
    31
    51

________________________________

[Ver No TheHuxley](https://thehuxley.com/problem/868?locale=pt_BR)