def calcular_digito(chave):
    n1, n2, n3 = chave.split('.')
    n3, n4 = n3.split("-")

    soma = int(max(list(n1))) + int(max(list(n2))) + int(max(list(n3)))
    resto = soma%10

    return str(resto)

resultados = []
entrada = input()

while entrada != "FIM":
    digito = calcular_digito(entrada)
    n4 = entrada.split('-')[-1]

    if digito == n4:
        resultados.append("VALIDO")
    else:
        resultados.append("INVALIDO")

    entrada = input()

for resultado in resultados:
    print(resultado)