# Controle de Calorias

## Descrição
As pessoas estão cada vez mais preocupadas com o corpo e muitas fazem o controle calórico dos alimentos que consomem. Entretanto, contar essas calorias é um trabalho chato e requer bastante atenção. Por isso, uma Nutricionista resolveu criar um programa que, a partir das calorias contidas em cada porção de alimento, dos alimentos consumidos e de uma meta calórica diária, indique a situação de seus clientes em relação a uma meta por ela estabelecida.

## Formato de entrada

A entrada se inicia com a leitura do nome do alimento (totalmente em caixa baixa e sem acentuações) e da quantidade de calorias (em kcal) em uma mesma linha e separados por uma vírgula. A entrada dos alimentos termina quando for digitada uma linha contendo um asterisco (*).

Em seguida, virão os casos de teste para contabilizar a ingestão calórica de cada pessoa. Um caso de teste é composto um inteiro T (1 ≤ T ≤ 100) indicando que a pessoa ingeriu diariamente T alimentos entre os alimentos cadastrados e um outro inteiro que consiste na meta calórica diária M (1 ≤ M ≤ 10000), separados entre si por um espaço em branco.

Finalmente, haverá T linhas com um inteiro N e o nome de um alimento (totalmente em caixa baixa e sem acentuações), indicando que a pessoa ingeriu uma quantidade N daquele alimento. A entrada termina com T = 0 e M = 0.

## Formato de saída

Para cada caso de teste (T), se o total de calorias ingeriras ultrapassou a Meta (M) correspondente, imprima “Acima da meta”. Caso tenha sido igual, imprima “Exatamente na meta” e caso tenha sido menor “Abaixo da meta”.

## Exemplos de:
_________________________________________
### Entrada
    iogurte light,50
    iogurte de morango,90
    iogurte de chocolate,120
    mamao,85
    manga,120
    goiaba,70
    *
    2 900
    10 iogurte light
    5 mamao
    1 2400
    20 manga
    3 1500
    1 manga
    10 iogurte de chocolate
    1 goiaba
    0 0

### Saída
    Acima da meta
    Exatamente na meta
    Abaixo da meta
_________________________________________
[Ver no The Huxley](https://thehuxley.com/problem/3082?quizId=7373)