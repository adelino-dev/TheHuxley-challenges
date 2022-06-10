# Ano novo!

## Descrição
Ambrosina está preparando uma série de festividades de fim de ano, portanto planeja fazer a ceia de natal, e a comemoração de ano novo, para como de costume, reunir toda a sua família.

Para a ceia de natal, ela precisa comprar comida, refrigerantes, e a decoração de natal.

Para a comemoração de ano novo, ela precisa comprar comida, refrigerantes, cerveja, e a decoração de ano novo.

Sabe-se que as lojas oferecem descontos, quando chega próximo a uma data festiva com a intenção de "queimar o estoque", e Ambrosina, querendo economizar, mas, sem querer acumular muito trabalho preparando as festividades, irá decidir duas datas para fazer as compras, uma antes do natal (compras do natal), e uma antes do ano novo (compras do ano novo).

Considere que o mês é dezembro.

Os descontos para o natal são:

- Antes do dia 20, sem desconto para comida, 10% de desconto para refrigerantes, e 15% de desconto para a decoração.
- Dia 20, 12% de desconto para comida, 15% de desconto para refrigerantes, e 20% de desconto para a decoração.
- Dia 21, 17% de desconto para comida, 22% de desconto para refrigerantes, e 27% de desconto para a decoração.
- Dia 22, 20% de desconto para comida, 22% de desconto para refrigerantes, e 30% de desconto para a decoração.
- Dia 23, 25% de desconto para comida, 29% de desconto para refrigerantes, e 35% de desconto para a decoração.
- Dia 24, 35% de desconto para comida, 35% de desconto para refrigerantes, e 50% de desconto para a decoração.

Os descontos para o ano novo são:

- Dia 25, 15% de desconto para comida, 13% de desconto para refrigerantes, sem desconto para cerveja, e 10% de desconto para a decoração.
- Dia 26, 19% de desconto para comida, 25% de desconto para refrigerantes, 5% de desconto para cerveja, e 23% de desconto para a decoração.
- Dia 27, 24% de desconto para comida, 30% de desconto para refrigerantes, 12% de desconto para cerveja, e 33% de desconto para a decoração.
- Dia 28, 30% de desconto para comida, 32% de desconto para refrigerantes, 20% de desconto para cerveja, e 35% de desconto para a decoração.
- Dia 29 e 30, 35% de desconto para comida, 40% de desconto para refrigerantes, 33% de desconto para cerveja, e 42% de desconto para a decoração.
- Dia 31, 40% de desconto para comida, 47% de desconto para refrigerantes, 45% de desconto para cerveja, e 66% de desconto para a decoração.

Sabendo dessas informações, Ambrosina vai decidir o melhor dia para fazer as compras de acordo com a sua necessidade, e gostaria que você calculasse o preço das compras de natal, de ano novo, e o total.


## Formato de entrada

Primeiro, Ambrosina irá lhe fornecer um valor inteiro D1(Dia de compra), onde (1 <= D1 <= 24), para fazer as compras de natal, seguido de 3 valores reais CO, RE, DE, que representam respectivamente o custo de: Comida, Refrigerante e Decoração.

Logo em seguida, Ambrosina irá lhe fornecer o segundo dia de compras D2, onde desta vez (25 <= D2 <= 31) para fazer as compras de ano novo, seguido de 4 valores reais CO, RE, CE, DE, que representam respectivamente o custo de: Comida, Refrigerante, Cerveja e Decoração.

dispostos da seguinte maneira:

    D1
    CO RE DE
    D2
    CO RE CE DE

## Formato de saída

Três valores reais com duas casas decimais, separados por uma quebra de linha.

Dispostos da seguinte maneira:

    Compras de natal: R$ N.
    Compras de ano novo: R$ A.
    Total das compras: R$ T.

Onde, N é o valor das compras de natal, A é o valor das compras de ano novo, e T o valor total das compras.


## Exemplos de:


| Entrada | Saída |
| -- | -- |
| 23 | Compras de natal: R$ 255.20. |
| 155.35 68.99 138|  Compras de ano novo: R$ 296.05. |
| 31 | Total das compras: R$ 551.24. |
| 197.58 85.45 147.66 150 |

[Ver no The Huxley](https://thehuxley.com/problem/2385)