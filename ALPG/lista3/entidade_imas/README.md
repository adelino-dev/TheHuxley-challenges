# A Entidade e os ímãs

## Descrição
A Entidade ganhou N ímãs no seu aniversário, ela achou muito interessante a forma como eles se atraem e repulsam. Certo dia ela estava andando num corredor com sua caixa de ímãs, e só no final do corredor, percebeu que a caixa estava furada. Todos os ímãs caíram, um ímã depois do outro. Mas ela achou muito interessante, pois formaram-se K grupos de ímãs, além disso, ela percebeu que existia um grupo com X ímãs.

Ela quer fazer algumas análises probabilísticas, mas ela não quer perder tempo contando quantos grupos e qual o maior grupo existe. Então, ela quer que você faça um programa que faça essa contagem por ela.

Exemplo: 6 ímãs caíram na seguinte ordem:
10
10
10
01
10
10



## Formato de entrada

A primeira linha da entrada conterá um inteiro N, a quantidade de ímãs que a Entidade ganhou de aniversário. Em seguida, virão N linhas, onde cada linha terá um código m, representando a orientação do ímã, se m for "10", o ímã tem o polo Norte apontado para esquerda, e se m for "01", o ímã tem o polo Norte apontando para direita.

## Formato de saída

A saída deverá conter a quantidade de grupos K de ímãs e o tamanho do maior grupo X de ímãs, a saída deve seguir a seguinte formatação:
"groups: K, biggest: X".

## Exemplos de:
___________________________________________
### Entrada
    6
    10
    10
    10
    01
    10
    10

### Saída
    groups: 3, biggest: 3
___________________________________________
### Entrada
    4
    01
    01
    01
    10

### Saída
    groups: 2, biggest: 3
___________________________________________
[Ver no The Huxley](https://thehuxley.com/problem/2203?quizId=7373)