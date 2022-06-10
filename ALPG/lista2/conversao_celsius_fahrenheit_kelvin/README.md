# Conversão Celsius, Fahrenheit e Kelvin

## Descrição
Faça um programa para converter um valor de temperatura em uma escala de mediada definida pelo usuário para as outras escalas de medida.

- Se o usuário fornecer uma temperatura em graus Celsius, imprima a mesma temperatura em Fahrenheit e Kelvin
- Se o usuário fornecer uma temperatura em graus Fahrenheit, imprima a mesma temperatura em Celsius e Kelvin
- Se o usuário fornecer uma temperatura em graus Kelvin, imprima a mesma temperatura em Fahrenheit e Celsius

## Formato de entrada

Uma escala de medida de temperatura ("C", "F" ou "K")

Um valor de temperatura a ser convertido

- Esse valor deve obedecer os seguintes valores mínimos (float):
    - Celsius: t >= -273.0
    - Fahrenheit: t >= -459,67
    - Kelvin: t >= 0.0
    - Se o usuário fornecer um valor menor que esses para cada temperatura, imprima uma mensagem de erro
        - "Valor de temperatura abaixo do minimo"
    - Não há limite máximo de temperatura


## Formato de saída

- Se o usuário fornecer uma temperatura em graus Celsius, imprima a mesma temperatura em Fahrenheit e Kelvin
- Se o usuário fornecer uma temperatura em graus Fahrenheit, imprima a mesma temperatura em Celsius e Kelvin
- Se o usuário fornecer uma temperatura em graus Kelvin, imprima a mesma temperatura em Fahrenheit e Celsius
- Se o usuário fornecer um valor menor que esses para cada temperatura, imprima uma mensagem de erro
    - "Valor de temperatura abaixo do minimo"

## Exemplos de:
_________________________________
### Entrada
    F
    34.0

### Saída
    1.11 C
    274.26 K
_________________________________
### Entrada
    K
    -8.0

### Saída
    Valor de temperatura abaixo do minimo
_________________________________
### Entrada
    K
    29.0

### Saída
    -244.15 C
    -407.47 F
_________________________________
## Entrada
    C
    -237.0
## Saída
    -394.60 F
    36.15 K
_________________________________
[Ver no The Huxley](https://thehuxley.com/problem/1080)