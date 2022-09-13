entrada = list(input())
caracteres = sorted(set(entrada))
caracteres.reverse()

for caracter in caracteres:
    qnt = entrada.count(caracter)
    print(caracter, qnt)