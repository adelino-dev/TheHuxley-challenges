# Controle de armas

## Descrição
O estado brasileiro deseja realizar o controle de armas na fronteira. Para ajudar nessa tarefa, você deve fazer um programa que determina se uma pessoa pode ultrapassar a fronteira com a quantidade de armas que ela leva.

Primeiro você deve receber se a nacionalidade da pessoa:

 - (B)rasileiro
 - (E)strangeiro
Em seguida, você deve receber a ocupação da pessoa, que pode ser:

 - (M)ilitar
 - (T)urista
 - (C)aminhoneiro
 - (O)utro
Depois você deve receber a quantidade de armas que a pessoa está carregando e qual o calibre da arma (ambos inteiros). Se a quantidade e o calibre forem zero é indivcativo que a pessao não está portando nenhuma arma.

Em seguida deve liberar ou barrar a entrada da pessoa de acordo com as seguintes regras:

Caso a pessoa seja estrangeira, ela só pode ser liberada se não estiver portando nenhuma arma.

Caso seja brasileira:
- Como militar, ela pode portar qualquer quantidade de armas de qualquer calibre que sua entrada é liberada.
- Como Turista, ou outro ela só pode portar uma única arma com calibre até o 22.
- Como Caminhoneiro, ela pode portar até 2 armas com calibre no máximo até o 38.


## Formato de entrada

A nacionalidade

A ocupação da pessoa

A quantidade de armas

O calibre da arma

## Formato de saída

"Liberado" ou "Barrado" de acordo com as regras descritas acima.

## Exemplos de:
___________________________________________
### Entrada
    E
    T
    0
    0

### Saída
    Liberado
___________________________________________
### Entrada
    E
    T
    1
    22

### Saída
    Barrado
___________________________________________
### Entrada
    B
    M
    5
    50

### Saída
    Liberado
___________________________________________
### Entrada
    B
    T
    1
    38

### Saída
    Barrado
___________________________________________
### Entrada
    B
    O
    1
    22
### Saída
    Liberado
___________________________________________
### Entrada
    B
    O
    0
    0
### Saída
    Liberado
___________________________________________
### Entrada
    B
    C
    3
    22

### Saída
    Barrado
___________________________________________

[Ver no The Huxley](https://thehuxley.com/problem/2145)