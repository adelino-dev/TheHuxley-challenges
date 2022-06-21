alimentos_calorias = {}
resultados = []

########### Coletando tabela calórica ###############

entrada = input()
while entrada != "*":
    entrada = entrada.split(',')
    alimento = entrada[0]
    calorias = int(entrada[1])
    alimentos_calorias[alimento] = calorias

    entrada = input()

########### Coletando alimentos ingeridos ###########

qnt_alimentos, meta = [int(i) for i in input().split()]
while qnt_alimentos+meta:
    calorias_ingeridas = 0
    for i in range(qnt_alimentos):
        entrada = input().split()
        qnt = int(entrada[0])
        alimento = " ".join(entrada[1:])
        calorias_ingeridas += qnt * alimentos_calorias[alimento]
    ############# Processando resultado ##############
    
    if calorias_ingeridas < meta:
        resultados.append("Abaixo da meta")

    elif calorias_ingeridas == meta:
        resultados.append("Exatamente na meta")

    else:
        resultados.append("Acima da meta")
    qnt_alimentos, meta = [int(i) for i in input().split()]
    
    

######WWWWWWW#### Imprimindo Resultados ###WWWWWWWWWWWW
for resultado in resultados:
    print(resultado)
