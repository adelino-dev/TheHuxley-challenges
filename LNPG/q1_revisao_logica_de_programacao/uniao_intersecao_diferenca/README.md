# União, interseção e diferença

Tempo máximo de execução: 1s

Tópicos: array, lógica matemática, repetição

## Descrição

Faça um programa que receba os elementos de 2 vetores e imprima na saída a união, a interseção e a diferença entre os 2 vetores.

## Formato de entrada

No começo o usuário informa 2 inteiros que determinam a quantidade de elementos dos 2 vetores. Em seguida, o usuário informa os elementos do vetor.

## Formato de saída

Os conjuntos união, interseção e diferença entre os vetores de acordo com os exemplos.

## Exemplos de:

### Entrada

    7
    3
    z
    x
    c
    f
    r
    t
    k
    p
    k
    j

### Saída

    ['p', 'k', 'j', 'z', 'x', 'c', 'f', 'r', 't']
    ['k']
    ['z', 'x', 'c', 'f', 'r', 't']

---------------------------------------------------

### Entrada

    5
    5
    a
    s
    d
    f
    g
    w
    s
    e
    d
    r

### Saída

    ['w', 's', 'e', 'd', 'r', 'a', 'f', 'g']
    ['s', 'd']
    ['a', 'f', 'g']


---------------------------------------------------

### Entrada

    0
    3
    qwe
    fgh
    c

### Saída

    ['qwe', 'fgh', 'c']
    []
    []


---------------------------------------------------

### Entrada

    3
    0
    qwe
    fgh
    c

### Saída

    ['qwe', 'fgh', 'c']
    []
    ['qwe', 'fgh', 'c']


---------------------------------------------------

### Entrada

    1
    1
    a
    a

### Saída

    ['a']
    ['a']
    []


---------------------------------------------------

### Entrada

    3
    4
    q
    w
    e
    q
    s
    w
    a

### Saída

    ['q', 's', 'w', 'a', 'e']
    ['q', 'w']
    ['e']


---------------------------------------------------

### Entrada

    3
    3
    a
    b
    c
    c
    d
    e

### Saída

    ['c', 'd', 'e', 'a', 'b']
    ['c']
    ['a', 'b']

[Ver no The Huxley](https://thehuxley.com/problem/3821?quizId=7901)