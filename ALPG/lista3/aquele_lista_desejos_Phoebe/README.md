# Aquele com a lista de desejos da Phoebe

## Descrição
Após seus 31 anos, Phoebe decidiu que precisava de uma forma melhor de organizar sua lista de desejos para cada idade. Sabendo que você é um ótimo programador, ela pediu para você escrever um programa que, dado os objetivos do ano e quais ela já completou, diga o que ela ainda precisa fazer.

![Mulher dizendo "Oh, my eyes, my eyes!!"](friends7.gif)


## Formato de entrada

A entrada consiste de é composta por:

- Inteiro N (0 <= N < 10), que corresponde a quantidade de coisas que a Phoebe quer fazer.
- N strings, uma por linha, na qual cada uma corresponde a uma coisa a ser feita.
- Inteiro M (0 <= M < 10), que corresponde a quantidade de coisas que a Phoebe já fez.
- M strings, uma por linha, na qual cada uma corresponde a uma coisa já feita.

Conhecendo a Phoebe, sabe-se que ela pode acabar tentando registrar coisas que não estavam na lista, neste caso, o registro é ignorado.

É garantido que nunca haverão objetivos repetidos na lista do que Phoebe quer fazer.

## Formato de saída

A saída deve seguir o formato, caso Phoebe não consiga atingir todos os objetivos:

    Ainda falta(m) K objetivo(s)!

Seguido pelos K objetivos restantes, um por linha, na ordem em que aparecem na entrada.

Caso Phoebe tenha completado todos os objetivos, a seguinte mensagem deve ser impressa:

    Smelly Cat, Smelly Cat, what are they feeding you?

## Exemplos de:
__________________________________________________________
### Entrada
    3
    Conhecer alguma pessoal de Portugal
    Ter o beijo perfeito
    Aula de franco-atirador
    1
    Ter o beijo perfeito

### Saída
    Ainda falta(m) 2 objetivo(s)!
    Conhecer alguma pessoal de Portugal
    Aula de franco-atirador
__________________________________________________________
### Entrada
    2
    Percorrer uma milha em uma bola saltitante
    Fazer as pazes com a irmã
    2
    Percorrer uma milha em uma bola saltitante
    Fazer as pazes com a irmã

### Saída
    Smelly Cat, Smelly Cat, what are they feeding you?
    
__________________________________________________________
[Ver no The Huxley](https://thehuxley.com/problem/2489?quizId=7373)