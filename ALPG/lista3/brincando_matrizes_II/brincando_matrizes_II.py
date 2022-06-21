matriz = []
diagonalOut = []
positivos = []

for i in range(9):
    elemento = int(input())
    matriz.append(elemento)

    if not(i in (0,4,8)):
        diagonalOut.append(elemento)

    if elemento>0:
        positivos.append(elemento)

media = sum(positivos)/len(positivos)
menor = min(matriz)
delta = 1 if menor%2 == 0 else 0
soma = sum(diagonalOut)

print("{:.2f}".format(media), menor, delta, soma)