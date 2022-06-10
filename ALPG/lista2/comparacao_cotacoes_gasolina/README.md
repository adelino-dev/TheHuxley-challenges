# Comparação de Cotações de Gasolina

## Descrição
Você cansou de tantas fake news sobre o preço da gasolina nos EUA e resolver calcular os valores por conta própria. Porém, descobriu que nos EUA a gasolina tem preço cotado em dólar/galão, enquanto que no Brasil é usado real/litro. Por isso, resolveu escrever um programa que realize as conversões e cálculos para você, facilitando a comparação dos preços da gasolina nos EUA e no Brasil.

O seu programa irá receber o valor em dólares de um galão de gasolina nos EUA (1 galão equivale a 3,7854 litros, mas para facilitar trabalhe com 3,8 litros), o valor em reais do litro no Brasil e a cotação do dólar em reais. Com base nisso, seu programa deve determinar o valor da gasolina nos EUA em reais/litro e informar aonde a gasolina está mais barata (ou se é igual).

## Formato de entrada

A entrada consiste de 3 linhas contendo:

Na primeira, o valor (número real) de um galão de gasolina nos EUA em dólares (U$);
Na segunda, o valor (número real) de um litro de gasolina no Brasil em reais (R$);
Na terceira, a cotação de um dólar em reais (número real).

## Formato de saída

A saída deve ser formada por 3 linhas contendo:

- Na primeira, o valor de um litro de gasolina nos EUA em reais;

- Na segunda, o valor de um litro de gasolina no Brasil em reais;

- Na terceira, uma das 3 opções de resultado: Mais barata nos EUA, Mais barata no Brasil ou Igual.

Verifique mais detalhes do formato nos exemplos. Os valores em reais devem ser arredondados com 2 casas decimais.

## Exemplos de:
____________________________________
### Entrada
    3.20
    4.49
    3.70

### Saída
    Gasolina EUA: R$ 3.12
    Gasolina Brasil: R$ 4.49
    Mais barata nos EUA
____________________________________
### Entrada
    3.30
    3.45
    4.00

### Saída
    Gasolina EUA: R$ 3.47
    Gasolina Brasil: R$ 3.45
    Mais barata no Brasil
____________________________________

[Ver no The Huxley](https://thehuxley.com/problem/2176)