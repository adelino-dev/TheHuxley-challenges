# Consulta IPCA

## Descrição
Escreva um programa que carregue os dados referentes ao IPCA (Índice Nacional de Preços ao Consumidor Amplo) e que permita fazer consultas sobre estes dados, considerando um certo período.

## Formato de entrada

A primeira linha da entrada informa um valor inteiro N que indica quantos meses de IPCA serão fornecidos nas N linhas seguintes da entrada.

Cada uma dessas N linhas possui a informação do ano/mês e o índice do IPCA (número real) separados entre si por espaço em branco. 

Observe que as informações do ano e do mês não são fornecidas necessariamente em ordem cronológica e que o valor do IPCA usa a vírgula para separar a parte inteira da decimal.Em seguida virão as consultas que podem ser de 2 tipos:

**M**: Mês específico, no qual o usuário informa o mês e o ano que deseja saber o valor do IPCA.

**P**: Período de dois ou mais meses do qual deseja a soma dos respectivos valores de IPCA. 

Neste caso, são informados o mês e o ano de início, além da quantidade de meses.As consultas se encerram quando for digitado o caractere * em uma linha.

## Formato de saída

Para cada consulta, deve ser fornecido o valor do IPCA no período com 2 casas decimais.

Para os tipos de consulta M e P, caso não se tenha a informação de algum mês, o programa deve imprimir na saída “Dados indisponiveis para este periodo”.

## Exemplos de:
___________________________________________

### Entrada

    15
    2021-02 0,86
    2021-01 0,25
    2021-03 0,93
    2021-04 0,31
    2021-05 0,83
    2021-06 0,53
    2021-07 0,96
    2021-08 0,87
    2021-09 1,16
    2021-10 1,25
    2021-12 0,73
    2021-11 0,95
    2022-01 0,54
    2022-02 1,01
    2022-03 1,62
    M 2/2021
    M 4/2022
    P 1/2021 3
    P 9/2021 4
    P 11/2021 3
    P 12/2021 5
    *

### Saída
    
    0.86
    Dados indisponiveis para este periodo
    2.04
    4.09
    2.22
    Dados indisponiveis para este periodo
___________________________________________

[Ver no The Huxley](https://thehuxley.com/problem/3988?quizId=7373)