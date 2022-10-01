especiais =  ('.', '"', '(', '*', '$', '#', ':') 

def remover_especiais(palavra):
    for especial in especiais:
        palavra = palavra.split(especial)
        palavra = " ".join(palavra)

    return palavra

def separar_palavras(texto):
    lista = []
    palavras = texto.split()

    for palavra in palavras:
        if not(palavra in especiais):
            palavras = remover_especiais(palavra).split()
            for palavra in palavras:
                lista.append(palavra.lower())
    
    lista.sort()
    return lista

def contar_palavras(lista):
    quantidades = {}
    palavras = sorted(set(lista))

    for palavra in palavras:
        quantidades[palavra] = lista.count(palavra)
    
    return quantidades


if __name__ == "__main__":
    entrada = input()
    texto = ""

    while entrada != "-1":
        texto += entrada + " "
        entrada = input()
    
    palavras = separar_palavras(texto)
    quantidades = contar_palavras(palavras)

    for palavra in quantidades:
        qnt = quantidades[palavra]
        print(palavra, qnt)