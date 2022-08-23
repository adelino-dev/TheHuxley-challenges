def getTamanhoMaior(numeros):
    maior = 0

    for i in set(numeros):
        tamanho = numeros.count(i)
        if tamanho > maior:
            maior = tamanho

    return maior
    
def getQuantidadeTorres(numeros):
    return len(set(numeros))

n = int(input())
numeros = [int(i) for i in input().split()]

maior = getTamanhoMaior(numeros)
quantidade = getQuantidadeTorres(numeros)

print(maior, quantidade)
