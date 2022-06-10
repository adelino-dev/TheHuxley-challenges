# Choque Elétrico

## Descrição
Ao tentar colocar um Voltorb em uma piscina, Biu acabou levando um choque do trovão.

Curioso de saber qual foi a intensidade do choque que levou ele pesquisou e descobriu que existia uma relação entre o level do voltorb e a potência de seu choque. Como descrito na tabela abaixo.

Escreva um programa que, dado o level do voltorb, imprima de quanto foi o choque em W segundo a tabela:

| Level | Potência (em W)|
| -- | -- |
| 1-20 |	20 + (level)3|
| 21-40 | 8000 + (level - 10)^2|
| 41-60	| 9000 + 5*level|
| 61-80	| 9300 + 2*level|
| 81-100 | 9500 + level|

## Formato de entrada

    L
- V - número natural menor que 100.
A linha única de entrada é composta pelo level do Voltorb.

obs: A entrada deve ser considerada amigável, ou seja, sempre estará no formato descrito.


## Formato de saída

    Potencia de: P W
- P - int

As linhas de saída são compostas por um texto seguido, seguido pela potência em W, com um texto indicando a unidade.


## Exemplos de:
_______________________________
### Entrada
    15

### Saída
    Potencia de : 3395 W

_______________________________
### Entrada
    50

### Saída
    Potencia de : 9250 W

_______________________________
## Entrada
    85

## Saída
    Potencia de : 9585 W
_______________________________

[Ver no The Huxley](https://thehuxley.com/problem/1169)