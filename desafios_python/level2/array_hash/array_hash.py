posicao_alfabeto = {
    'A': 0, 'B': 1, 'C': 2, 
    'D': 3, 'E': 4, 'F': 5, 
    'G': 6, 'H': 7, 'I': 8, 
    'J': 9, 'K': 10, 'L': 11, 
    'M': 12, 'N': 13, 'O': 14, 
    'P': 15, 'Q': 16, 'R': 17, 
    'S': 18, 'T': 19, 'U': 20, 
    'V': 21, 'W': 22, 'X': 23, 
    'Y': 24, 'Z': 25
    }

num_testes = int(input())
valores = []

for index_teste in range(num_testes):
    num_linhas = int(input())
    valor = 0
    for index_linha in range(num_linhas):
        letras = input()
        posicao_elemento = 0
        for letra in letras:
            # Valor = (Posição no alfabeto) + (Elemento de entrada) + (Posição do elemento) 
            valor +=  posicao_alfabeto[letra] + index_linha + posicao_elemento
            posicao_elemento += 1
    valores.append(valor)
    
for valor in valores:
    print(valor)