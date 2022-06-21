# Controle de estoque

## Descrição
Em um estoque são dados os códigos das mercadorias e as respectivas quantidades existentes. A seguir, são fornecidos os pedidos dos clientes. O seu objetivo  é fazer um programa de controle do estoque que:

- Leia o estoque inicial (máximo de 100 mercadorias);
- Leia os pedidos dos clientes, constituído, cada um, de: número do cliente; código da mercadoria e quantidade desejada;
- Seja verificado, para cada pedido, se ele pode ser atendido integralmente. Caso possa ser atendido, imprima OK, caso contrário ESTOQUE INSUFICIENTE;
- Ao final da execução do programa, imprima o estoque final;

## Formato de entrada

Uma lista de inteiros n e m, indicando o código da mercadoria e a quantidade dessa mercadoria disponível no estoque, respectivamente.

Essa lista se encerra quando n for igual a 9999.

Depois será dada uma lista de inteiros i, j e k, onde i corresponde ao número do cliente, j é o código da mercadoria sendo solicitada e k a quantidade pedida.

Os pedidos se encerram quando i for igual a 9999.

## Formato de saída

Para cada pedido, a saída deve imprimir OK ou ESTOQUE INSUFICIENTE, seguida de um final de linha.

Ao final dos pedidos, deve ser impresso uma lista de inteiros x, y correspondendo ao código e ao estoque restante das mercadorias.

Cada par x, y dever ser impresso em uma linha.

## Exemplos de:
___________________________________
### Entrada

    1 3
    5 40
    8 10
    9999
    1 1 2
    1 1 1
    1 1 1
    10 8 4
    9999

### Saída

    OK
    OK
    ESTOQUE INSUFICIENTE
    OK
    1 0
    5 40
    8 6
___________________________________
[Ver no The Huxley](https://thehuxley.com/problem/71?quizId=7373)