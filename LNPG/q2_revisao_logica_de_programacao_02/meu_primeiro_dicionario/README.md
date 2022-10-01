# Meu Primeiro Dicionário

Tempo máximo de execução: 1s

Tópicos: substrings, ciclos, string, dicionário

## Descrição

Andy de apenas 8 anos tem um sonho - ele deseja criar o seu próprio dicionário. Isto não é uma tarefa fácil para ele, pois conhece poucas palavras. Bem, ao invés de pensar nas palavras que sabe, ele teve uma ideia brilhante. A partir do seu livro de histórias favorito, ele vai criar um dicionário com todas as palavras distintas que existem nele. Ordenando estas palavras em ordem alfabética, o trabalho estará feito. É claro, isso é uma tarefa que toma um certo tempo e, portanto, a ajuda de um programador de computador como você é muito bem-vinda.

Você foi convidado a escrever um programa que liste todas as diferentes palavras que existem em um texto. Neste caso, uma palavra é definida como uma sequência de letras, maiúsculas ou minúsculas. Palavras com apenas uma letra também deverão ser consideradas. Portanto, seu programa deverá ser "CaSe InSeNsItIvE". Por exemplo, palavras como "Apple", "apple" ou "APPLE" deverão ser consideradas como a mesma palavra.


## Formato de entrada


A entrada contém no máximo 10.000 linhas de texto, cada uma delas com no máximo 200 caracteres. O fim de entrada é determinado por -1.

O conjunto de caracteres especiais que devem ser excluídos é formado apenas por: . " ( * $ # : 

Para remover estes caracteres especiais, deve ser criada uma função chamada remover_especiais com apenas um parâmetro, do tipo string, chamado de palavra. A função deve retornar um valor, também do tipo string, contendo a palavra sem os caracteres especiais.

## Formato de saída

Você deve imprimir uma lista de diferentes palavras que aparecem no texto, uma palavra por linha. Todas as palavras devem ser impressas com letras minúsculas, em ordem alfabética e com a quantidade de vezes que elas aparecem no texto. Deverá haver no máximo 5000 palavras distintas.

## Exemplos de:

### Entrada

    Ex(*a#.mpl.e:
    Adventures in Disneyland
    Two blondes were going to Disneyland when they came to a fork in the road. The sign read: "Disneyland LEFT."
    So they went home.
    -1

### Saída:

    a 2
    adventures 1
    blondes 1
    came 1
    disneyland 3
    e 1
    ex 1
    fork 1
    going 1
    home 1
    in 2
    left 1
    mpl 1
    read 1
    road 1
    sign 1
    so 1
    the 2
    they 2
    to 2
    two 1
    went 1
    were 1
    when 1

-----------------------------------
[Ver no TheHuxley](https://thehuxley.com/problem/3751?quizId=7972)