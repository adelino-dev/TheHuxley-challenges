# Dificuldades em Bhaskara

## Descrição
Em meio aos seus estudos diários, Ambrósio notou que calcular a Fórmula de Bhaskara demanda muito tempo. Querendo agilizar seu processo de aprendizagem, ele pediu que você o ajudasse criando um programa que, dado N equações do segundo grau, imprima as raízes de cada equação (x1 e x2).

OBS: Cuidado com a precisão de ponto flutuante.

## Formato de entrada

A primeira linha contém N, onde N é o número de equações do segundo grau que serão resolvidas.

Seguida por N linhas, onde cada uma contém:

Ax^2 + Bx + C, onde A, B e C são os coeficientes da função do segundo grau.

## Formato de saída

Para cada uma das i-ésimas equações do segundo grau a saída esperada é:

Test i: Ax^2 + Bx + C

0 raízes: uma única linha contendo: "SEM RESPOSTA".

1 raiz: uma única linha contendo: "X = raiz".

2 raízes: duas linhas contendo: "X1 = raiz1" e "X2 = raiz2" respectivamente.

Além disso, os valores das raízes devem ser dados com 2 casas de aproximação.

## Exemplos de:

### Entrada


4
-7x^2 + -6x + 3
-4x^2 + 4x + -1
7x^2 + -6x + 2
1x^2 + 0x + -16
Saída


Test 1: -7x^2 + -6x + 3
X1 = -1.21
X2 = 0.35

Test 2: -4x^2 + 4x + -1
X = 0.50

Test 3: 7x^2 + -6x + 2
SEM RESPOSTA

Test 4: 1x^2 + 0x + -16
X1 = 4.00
X2 = -4.00
 
## Formato de entrada

A primeira linha contém N, onde N é o número de equações do segundo grau que serão resolvidas.

Seguida por N linhas, onde cada uma contém:

Ax^2 + Bx + C, onde A, B e C são os coeficientes da função do segundo grau.

## Formato de saída

Para cada uma das i-ésimas equações do segundo grau a saída esperada é:

Test i: Ax^2 + Bx + C

0 raízes: uma única linha contendo: "SEM RESPOSTA".

1 raiz: uma única linha contendo: "X = raiz".

2 raízes: duas linhas contendo: "X1 = raiz1" e "X2 = raiz2" respectivamente.

Além disso, os valores das raízes devem ser dados com 2 casas de aproximação.

## Exemplos de:
__________________________________________________
### Entrada
    4
    -7x^2 + -6x + 3
    -4x^2 + 4x + -1
    7x^2 + -6x + 2
    1x^2 + 0x + -16

### Saída
    Test 1: -7x^2 + -6x + 3
    X1 = -1.21
    X2 = 0.35

    Test 2: -4x^2 + 4x + -1
    X = 0.50

    Test 3: 7x^2 + -6x + 2
    SEM RESPOSTA

    Test 4: 1x^2 + 0x + -16
    X1 = 4.00
    X2 = -4.00
__________________________________________________ 
[Ver No The Huxley](https://thehuxley.com/problem/2051?quizId=7373)