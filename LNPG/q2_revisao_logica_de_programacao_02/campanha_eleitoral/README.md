# Campanha Eleitoral

Tempo máximo de execução: 1s

Tópicos: decisão, entrada formatada, repetição

## Descrição

Uma agência de publicidade cria anúncios para candidatos em vários meios de comunicação. Os preços são calculados em função das mídias escolhidas, que podem ser: internet, rádio, tv, revista e outdoor.

- Anúncios para Internet custam R$ 3.000, para revista R$ 750 e para outdoor R$ 1.500;

- Anúncios para rádio custam R$ 500 se for para FM, e R$ 300 se for para AM;

- Anúncios para tv custam R$ 1.200 em horário regular (até 20h) e R$ 2000 em horário nobre (depois de 20h).

Escreva um programa que calcule qual será o custo total da propaganda escolhida pelos candidatos.

## Formato de entrada

O programa deve receber como entrada o primeiro nome do candidato junto com a quantidade de mídias em que deseja ter sua propaganda eleitoral divulgada. Nas linhas seguintes serão lidas as informações sobre os tipos de mídia que podem ser: internet, radio, tv, revista e outdoor. Quando houver informação adicional, esta será fornecida na linha seguinte (como no caso da rádio que pode ser fm ou am). O programa faz isso até que seja informado um candidato com

## Formato de saída

A saída consiste de uma linha para cada candidato, contendo seu nome seguido do caractere dois pontos (:), um espaço em branco e o custo da propaganda (ponto flutuante com 2 casas decimais).

## Exemplos de:

------------------------------

### Entrada

    Dilma 4
    internet
    radio
    am
    outdoor
    revista
    Aecio 2
    internet
    tv
    21
    FIM

### Saída

    Dilma: 5550.00
    Aecio: 5000.00

------------------------------

### Entrada

    Tiririca 2
    tv
    20
    radio
    fm
    FIM

### Saída


    Tiririca: 1700.00
------------------------------
[Ver no TheHuxley](https://thehuxley.com/problem/931?quizId=7972s)