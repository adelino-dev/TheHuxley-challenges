num_aprovados =  0

num = 1 # 1 para nota de PT, 2 para matemática e 3 para Redação
aprovado = True #Estado atual do aluno que irá ser analisado

entrada = float(input())
while entrada >= 0:
   
    if num == 1: #Se a nota for de Português

        if entrada/50 < 0.8:
            aprovado = False

        num += 1

    elif num == 2: #Se a nota for de Matemática

        if entrada/35 < 0.6:
            aprovado = False

        num += 1

    else: # Se a nota for da redação

        if entrada < 7:
            aprovado = False

        if aprovado:
            num_aprovados += 1

        num = 1

    entrada = float(input())

print(num_aprovados)    