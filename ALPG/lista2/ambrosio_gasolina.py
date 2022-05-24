import math

entrada = [int(i) for i in input().split()]

distancia = entrada[0]
reais = entrada[1]
capacidade_litros = entrada[2]
num_postos = entrada[3]
preco_gasolina =  entrada[4]


litros_necessarios = distancia/10
litros_faltantes = litros_necessarios - capacidade_litros
if litros_faltantes < 0:
    litros_faltantes = 0
gastos = litros_faltantes*preco_gasolina + capacidade_litros*preco_gasolina

distancia_inicial_percorrivel = capacidade_litros*10
if distancia == 0:
    print("Pode viajar.")
    print("R$:", int(gastos))
        
elif capacidade_litros == 0:
    print("Nao pode viajar.")
    
elif (num_postos == 0):
    if distancia_inicial_percorrivel <= distancia:
        print("Pode viajar.")
        print("R$:", int(gastos))
    else:
        print("Nao pode viajar.")
    
elif gastos > reais:
    print("Nao pode viajar.")

else:
    distancia_postos = distancia/num_postos

    paradasNecessarias = math.ceil(litros_faltantes/capacidade_litros)
    num_postos -= (distancia_inicial_percorrivel//distancia_postos)

    if num_postos < paradasNecessarias:
        print("Nao pode viajar.")

    else:
        print("Pode viajar.")
        print("R$:", int(gastos))