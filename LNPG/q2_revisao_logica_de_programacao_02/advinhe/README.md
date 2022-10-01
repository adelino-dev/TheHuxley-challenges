# Adivinhe

Tempo máximo de execução: 3s

Tópicos: multiplas entradas, array, decisão, caractere, string

## Descrição

O jogo da adivinhação foi criado por um engenheiro de telecomunicações chamado Mordechai Meirovitz, na Romênia em 1971. O jogo ganhou o prestigiado prêmio do "Jogo do Ano" em 1974 e foi um enorme sucesso comercial, sendo vendido em mais de 40 países.

Trata-se de um jogo de lógica cujo seu objetivo como jogador é descobrir a senha secreta escolhida por um oponente. A senha a ser descoberta é formada por uma seqüência de caracteres de algum alfabeto. Para descobrir qual foi a senha, você "chuta" uma provável senha para o seu oponente. O chute é uma sequência de caracteres com o mesmo número de caracteres da senha. E os caracteres devem pertencer ao mesmo alfabeto.

Após cada chute seu, você receberá uma resposta, que consiste de 2 inteiros (E,B) indicando o quão bom foi o seu chute. Se um caractere do chute existe na senha na mesma posição (da string), então ele conta como "excelente" (E). Caso contrário, se o caractere existe na senha, mas em uma posição diferente, ele conta como "bom" (B). Um dado caractere do chute não é contado duas vezes (ou seja, se ele foi contado como excelente, não é contado como bom). A tabela abaixo ilustra o jogo com alguns exemplos.


![Tabela](https://thehuxley.com/api/v1/problems/image/c37d64f33a4d9b9f3df6c2d14f187e7d.png)


Baseado nas respostas recebidas, o jogador pode deduzir qual foi a senha escolhida pelo oponente. O objetivo do jogo é encontrar a senha com o número mínimo de chutes.

Já o seu objetivo é um pouco mais simples: escrever um programa que receba a senha do primeiro jogador e em seguida recebe os chutes do segundo jogador. Você deve fornecer as respostas de acordo com o explicado acima.

## Formato de entrada

A primeira linha da entrada consiste de um número K representando o número de jogos que serão realizados. A próxima linha consiste de um número N, [0 < N < 8], representando o tamanho da senha a ser utilizada no próximo jogo. A próxima linha contém uma senha contendo dígitos, entre 1 e 7, com exatamente N caracteres que será utilizada no jogo em questão.

As próximas linhas contêm os chutes dados pelo segundo jogador e, portanto, consistem de uma sequência de dígitos, entre 1 e 7, com exatamente N caracteres. Cada jogo termina quando a senha é acertada ou quando o jogador desiste de tentar digitando uma seqüência de N caracteres '0'. Após cada jogo, o próximo jogo tem inicio a partir da leitura de uma linha contendo um inteiro indicando o tamanho da próxima senha. Na linha seguinte é dada a nova senha e o jogo prossegue com os chutes.

## Formato de saída

Para cada chute, seu programa deve imprimir (E,B), correspondendo ao número de excelentes e bons respectivamente.

## Exemplos de:

### Entrada

    2
    4
    1356
    6531
    4327
    1367
    1356
    3
    543
    132
    543

### Saída

    (0,4)
    (1,0)
    (2,1)
    (4,0)
    (0,1)
    (3,0)

[Ver no TheHuxley](https://thehuxley.com/problem/85?quizId=7972)