# Avaliação das notas de uma turma

Tempo máximo de execução: 1s

Tópicos: array, entrada formatada, repetição, dicionário, formatação


## Descrição

Escreva um programa para ler as resposta de uma turma em uma prova com 5 questões e, a partir do gabarito fornecido ao final, obter a maior nota, a menor nota e a média das notas da turma.

Para cada aluno pode haver mais de uma resposta, prevalecendo a última,ou seja, a(s) resposta(s) anterior(es) devem ser desconsideradas, não entrando portando no cálculo da maior/menor nota e média da turma. Para isso, é fornecido o primeiro nome do aluno junto com sua resposta, separados por um espaço em branco.

Para efeito de cálculo da nota do aluno, deve ser definida uma função chamada calcular_nota, a qual deve receber 2 parâmetros: a resposta do aluno e o gabarito da prova. Esta função deve retornar um valor inteiro que representa a nota do aluno (de 0 a 5).

## Formato de entrada

O programa deve os dados das respostas dos alunos (Primeiro Nome e Respostas). O primeiro nome e as respostas às 5 questões são informadas na mesma linha e separadas por um espaço em branco. A leitura dos dados dos alunos se encerra quando é encontrado o caractere *. Na linha seguinte é fornecido o gabarito das 5 questões.



## Formato de saída

A saída consiste de 3 linhas contendo, respectivamente: a maior nota (de 0 a 5), a menor menor nota (de 0 a 5) e a média das notas da turma (0.00 a 5.00). Observe que a média possui 2 casas decimais.



## Exemplos de:

### Entrada

    Jose abbde
    Pedro abbde
    Maria abddd
    Jose abcde
    Maria bbbbb
    Julia aaaaa
    *
    abcde


### Saída

    Maior: 5
    Menor: 1
    Media: 2.75

------------------------
[Ver no TheHuxley](https://thehuxley.com/problem/1285?quizId=7972)