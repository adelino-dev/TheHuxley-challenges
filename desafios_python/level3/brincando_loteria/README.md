# Brincando de Loteria

**Dificuldade: Médio**

_Tempo máximo de execução: 1s_

_Tópicos: array, decisão, repetição, dicionário_

## Descrição

Um grupo de amigos se reuniu para brincar de loteria. Cada amigo podia apostar em até 10 números diferentes (entre 1 e 100). Depois de todos apostarem, eram sorteados os números. Com base nas apostas e nos números sorteados, o objetivo era calcular o número de acertos de cada um e imprimir o resultado ordenado de forma crescente pelo número de acertos. Havendo empate, a ordem era definida pelo nome.

## Formato de entrada

O programa deve ler um número qualquer de apostas, sendo uma por linha. Cada linha é formada pelo primeiro nome do apostador, de um espaço em branco e de uma sequência de números (entre 1 e 100) separados entre si por um espaço em branco. Chega-se ao fim da leitura das apostas quando se encontra uma linha com a string FIM.Depois de concluída a leitura das apostas, deve ser lido o resultado do sorteio, que pode ter de 1 a 10 números (com valores entre 1 e 100) separados entre si por um hifens.

## Formato de saída

A saída consiste de uma relação de apostadores e seus acertos, sendo que o número acertos é representado pelo uso do caractere '+' (por exemplo, para 3 acertos seria +++). A relação deve ser ordenada de forma crescente pelo número de acertos. Em caso de empate, define-se a ordem pelo nome dos apostadores.

## Exemplos de:

### Entrada


    Alberto 5 4 3 50 25 10
    Jose 4 3 90 95
    Pedro 5 4 3 50 25 10
    Maria 4 3 90 95
    Antonio 12 15 20
    Aldo 10 20 30 40 50 60 70 80 90 100
    Breno 1 2 3 4 5 6 7 8 9 10
    Catarina 5 10 15 20
    FIM
    5-4-3-12-100

### Saída

    Aldo +
    Antonio +
    Catarina +
    Jose ++
    Maria ++
    Alberto +++
    Breno +++
    Pedro +++

_________________________________________________

### Entrada

    Alberto 5 4 3 50 25 10
    Jose 4 3 90 95
    Pedro 5 4 3 50 25 10
    Maria 4 3 90 95
    Antonio 12 15 20
    FIM
    5-4-3-12-100

### Saída

    Antonio +
    Jose ++
    Maria ++
    Alberto +++
    Pedro +++

_______________________________________________________

### Entrada

    Aldo 10 20 30 40 50 60 70 80 90 100
    Breno 1 2 3 4 5 6 7 8 9 10
    Catarina 5 10 15 20
    Maria 10
    FIM
    5-10-20

### Saída

    Maria +
    Aldo ++
    Breno ++
    Catarina +++

___________________________________________________________

[Ver no TheHuxley](https://thehuxley.com/problem/2253?locale=pt_BR)