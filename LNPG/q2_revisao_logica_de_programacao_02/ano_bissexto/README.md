# Ano Bissexto (no futuro)

Tempo máximo de execução: 1s

Tópicos: função

## Descrição

Estamos no ano de 2152.

Você foi contratado(a) para criar um programa que utilize funções para indicar se um determinado ano é ou não bissexto. Para cada ano fornecido ao programa, faz-se necessário, primeiro, identificar se o ano fornecido é um valor inteiro de 4 dígitos e, segundo, dado que o ano é um número válido, informar se é ou não um ano bissexto. 

Um ano é bissexto se ele satisfaz as seguintes condições:
* É divisível por 4 e,
* Não é divisível por 100 ou é divisível por 400.

Seu programa deve ter na solução três funções (3): contarDigitos, ehBissexto e Mensagem. A quantidade de parâmetros e retornos das funções ficam a critério do(a) programador(a).

## Formato de entrada

A entrada consiste numa lista de valores por linha. 

A entrada -1 indica o fim do programa.



## Formato de saída

Para cada valor da entrada uma mensagem deve ser exibida.

* Se o valor é um ano bissexto e for o ano atual: O ano xxxx eh bissexto
* Se o valor é um ano bissexto mas for um ano anterior ao ano atual: O ano xxxx foi bissexto
* Se o valor é um ano bissexto mas for um ano posterior ao ano atual: O ano xxxx serah bissexto
* Se o valor não é um ano bissexto: O ano xxxx NAO eh bissexto
* Se o número não é um ano de 4 dígitos: Ano invalido

## Exemplos de:

--------------------------------------

### Entrada

    1976
    -1

### Saída

    O ano 1976 foi bissexto

--------------------------------------

### Entrada

    2152
    02
    88
    -1

### Saída

    O ano 2152 eh bissexto
    Ano invalido
    Ano invalido

--------------------------------------

### Entrada

    2012
    208
    1987
    3504
    -1

### Saída

    O ano 2012 foi bissexto
    Ano invalido
    O ano 1987 NAO eh bissexto
    O ano 3504 serah bissexto
    
--------------------------------------

[Ver no TheHuxley](https://thehuxley.com/problem/3725?quizId=7972)