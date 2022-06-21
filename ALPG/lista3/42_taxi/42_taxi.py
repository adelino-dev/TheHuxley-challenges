corridas = int(input())
resultados = []
for i in range(corridas):
    distancia, custo = map(float, (input().split()))
    valor = distancia*custo

    eh_primo = True
    for num in range(2, (int(valor//1))):
        if (valor//1)%num == 0:
            eh_primo = False
            break

    if eh_primo:
        valor -= valor*0.42 
    resultados.append(valor)

for valor in resultados:
    print("%.2f"% valor)