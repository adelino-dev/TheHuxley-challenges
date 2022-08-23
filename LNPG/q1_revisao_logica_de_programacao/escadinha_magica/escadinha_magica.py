n = int(input())

for x in range(n):
    linha = []
    for y in range(1, x+2):
        linha.append(str(y))
    print(" ".join(linha))