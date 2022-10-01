def comparar(senha, chute):
    excelentes = 0
    bons = 0

    analisadas = ''

    for i in range(len(chute)):
        c = chute[i]
        s = senha[i]

        if c == s:
            excelentes += 1

        elif c in senha and not(c in analisadas):
            bons += 1
        
        analisadas += c
    
    return (excelentes, bons)

rodadas = int(input())
resultados = []

for rodada in range(rodadas):
    numCaracteres = int(input())
    senha = input()

    while True:
        chute = input()
        if int(chute) == 0:
            break

        else:
            resultado = comparar(senha, chute)
            resultados.append(resultado)

            if chute == senha:
                break

for resultado in resultados:
    print("(%i,%i)" % resultado)