entrada = [int(i) for i in input().split()]

distancia = entrada[0]
reais = entrada[1]
capacidade_litros = entrada[2]
num_postos = entrada[3]
preco_gasolina =  entrada[4]


distancia_inicial_percorrivel = capacidade_litros*10

if distancia_inicial_percorrivel >= distancia:
    print("Pode viajar.")
    print("R$: %.0f" % (reais))

else:
    litros_necessarios = distancia/10 #200/10 = 20
    litros_faltantes = litros_necessarios - capacidade_litros
    if litros_faltantes < 0:
        litros_faltantes = 0
    gastos = litros_faltantes*preco_gasolina
    distancia_postos = distancia//(num_postos+1)

    if (gastos <= reais) and (distancia_inicial_percorrivel >= distancia_postos):
        print("Pode viajar.")
        print("R$: %.0f" % (reais-gastos))

    else:
        print("Nao pode viajar.")