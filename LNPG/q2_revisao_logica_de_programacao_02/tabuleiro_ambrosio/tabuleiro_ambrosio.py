def calc_jogadas(ultimaCasa):
	jogadas = 0
	casaAtual = 1
	numSorteado = 0
	
	while casaAtual != ultimaCasa:
		jogadas += 1
		numSorteado += 1
		
		if numSorteado > 6:
			numSorteado = 1
		
		casaAtual += numSorteado
		
		if  casaAtual > ultimaCasa:
			casaAtual = casaAtual - ultimaCasa
		
	return jogadas


if __name__ == "__main__":
	casas = int(input())
	jogadas = calc_jogadas(casas)
	print(jogadas)