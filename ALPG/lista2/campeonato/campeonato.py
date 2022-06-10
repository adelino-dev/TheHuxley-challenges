vitoriasCormengo, empatesComengo, saldoComengo, vitoriasFlaminthians, empatesFlaminthians, saldoFlaminthians = [int(i) for i in (input().split())]

pontuacaoCormengo = vitoriasCormengo*3 + empatesComengo
pontuacaoFlaminthians = vitoriasFlaminthians*3 + empatesFlaminthians

if pontuacaoCormengo > pontuacaoFlaminthians:
    print("C")

elif pontuacaoFlaminthians > pontuacaoCormengo:
    print("F")

else:
    if saldoComengo > saldoFlaminthians:
        print("C")
    elif saldoFlaminthians > saldoComengo:
        print("F")
    else:
        print("=")