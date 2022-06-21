# Calculando o CRE

## Descrição
O Coeficiente de Rendimento Escolar (CRE) é calculado semestralmente e corresponde à média ponderada das notas finais obtidas em cada disciplina cursada, com aprovação ou não. O peso corresponde à carga horária total das disciplinas. O Coeficiente de Rendimento Escolar é determinado pela seguinte expressão: 

CRE= ((N1xH1) + (N2xH2) + … + (Nk x Hk))/(H1+H2+H3+...+Hk)

onde: Nk= Nota da disciplina k e Hk= Carga horária da disciplina k.

As notas devem ser consideradas numa escala de 0 a 100.

OBS:Não são considerados no cálculo do CRE: 


- Disciplinas trancadas (T)

- Aproveitamento de Disciplinas (AD)

- Disciplinas excluídas (DE)

- Aceleração de estudos (AE)

- Disciplinas dispensadas (DD)

- **Disciplinas em curso (DC)**


Exemplo: Considerando o histórico a seguir, ao final do primeiro semestre o CRE do aluno será: 

((50x53) + (33x45)+(50x64))/(50+33+50) = 55,15 

| SEMESTRE | DISCIPLINA | CH | NOTA | SITUAÇÃO |
| -- | -- | -- | -- | -- |
| 1 | Cálculo Aplicado | 83 | 70 | Aproveitamento de Disciplina |
| 1 | Relações Humanas no Trabalho | 50 | 53 | Aprovado|
| 1 | Introdução a Pesquisa Científica | 33 | 45 | Reprovado|
| 1 | Empreendedorismo | 50 | 64 | Aprovado |
| 2 | Português Instrumental | 67 | 30 | Reprovado por Falta |
| 2 | Inglês Instrumental | 67 | 61 | Aproveitamento de Disciplina |
| 2 | Algoritmos Estruturados | 83 | 90 | Aprovado |
| 2 | Redes de Computadores | 83 | 70 | Aceleração de Estudos |

O objetivo é escrever um algoritmo para calcular o CRE de um aluno a partir dos dados de entrada.

## Formato de entrada

- Um número inteiro representando o semestre da disciplina
- Um número inteiro representando a carga horária da disciplina (possibilidades: 33, 50, 67, 83).
- um número inteiro de 0 a 100, inclusive, representando a nota obtida na disciplina
- uma string indicando a situação da disciplina:
    * Aprovado (A)
    * Reprovado ( R)
    * Reprovado por falta (RF)
    * Disciplina trancada (DT)
    * Aproveitamento de Disciplina (AD)
    * Disciplinas excluídas (DE)
    * Aceleração de estudos (AE)
    * Disciplina dispensada (DD)
    * Disciplina em curso (DC) 

O usuário deverá informar uma ou mais disciplinas. Considerar como condição de parada quando o semestre for igual ou menor a zero ou maior que 10.


## Formato de saída

- O valor do CRE do aluno (float com duas casas decimais)

    Quando o usuário informar valor inválido para o semestre ou não for possível calcular o CRE, apresentar como saída a mensagem **_entrada invalida._**


## Exemplos de:

___________________________________________
### Entrada
    1
    83
    70
    AD
    1
    50
    53
    A
    0

### Saída
    53.00
___________________________________________

### Entrada
    1
    83
    70
    AD
    1
    50
    53
    A
    1
    33
    45
    R
    1
    50
    64
    A
    11

### Saída
    55.15
___________________________________________

### Entrada
    1
    83
    70
    AD
    1
    50
    53
    A
    1
    33
    45
    R
    1
    50
    64
    A
    2
    67
    30
    RF
    2
    67
    61
    AD
    2
    83
    90
    A
    2
    83
    70
    AE
    11

### Saída 
    59.42
___________________________________________

### Entrada
    12

### Saída
    entrada invalida
___________________________________________

### Entrada
    1
    33
    45
    AE
    1
    50
    64
    AD
    2
    83
    70
    AE
    0

### Saída
    entrada invalida
___________________________________________
### Entrada
    1
    83
    70
    A
    2
    50
    53
    R
    2
    57
    90
    A
    3
    83
    90
    AE
    0

### Saída
    63.61
___________________________________________
[Ver no The Huxley](https://thehuxley.com/problem/2353?quizId=7373)