# Contagem de dígitos

## Descrição
Diana escreverá uma lista com todos os inteiros positivos entre A e B, inclusive. Os inteiros não possuem zero à esquerda. 

Porém, Diana irá ser paga de acordo com a quantidade de dígitos que ela irá utilizar. Para isso, ela precisa saber quantas vezes ela utilizou cada um dos 10 dígitos dos números decimais. Por exemplo, se os inteiros dados foram 9 e 13, então a lista será: 9, 10, 11, 12 e 13. Nesse caso, diana utilizou o dígito 0 uma vez, o 1 cinco vezes, o 2 uma vez, o 3 uma vez e o 9 uma vez.

## Formato de entrada

Cada caso de teste é dado em uma única linha que contém dois inteiros A e B (1 <= A <= B <= 100000000). O último caso de teste é seguido por uma linha contendo dois zeros.

## Formato de saída

Para cada caso de teste, imprima uma única linha com 10 inteiros representando o número de vezes que cada dígito é usado ao escrever todos os inteiros entre A e B. Escreva a contagem de cada dígito em ordem crescente do 0 até o 9.

## Exemplos de:

___________________________________
### Entrada
    1 9
    12 321
    5987 6123
    12345678 12345679
    0 0

### Saída
    0 1 1 1 1 1 1 1 1 1
    61 169 163 83 61 61 61 61 61 61
    134 58 28 24 23 36 147 24 27 47
    0 2 2 2 2 2 2 2 1 1
___________________________________
[Ver no The Huxley](https://thehuxley.com/problem/236?quizId=7373)