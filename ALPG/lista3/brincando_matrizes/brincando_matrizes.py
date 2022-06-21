matriz = []
for i in range(9):
    matriz.append(int(input()))

media = sum(matriz)/9
maior = max(matriz)
if maior>0:
    delta = 1

elif maior<0:
    delta = -1

else:
    delta = 0

soma = matriz[0] + matriz[4]+ matriz[8]
print(("%.2f" % media), maior, delta, soma)