cardapio = {
    "Lasanha":8.00,
    "Estrogonofe":11.0,
    "Refrigerante":3.0,
    "Suco":2.5
}

comida = input().title()
bebida = input().title()

preco = cardapio[comida]+cardapio[bebida]
print("{:.2f}".format(preco))