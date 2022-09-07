dicionario = {
    "a":"@", "A": "@",
    "e":"3", "E": "3",
    "i":"1", "I": "1",
    "o":"0", "O": "0",
    "t":"7", "T": "7",
    "s":"5", "S": "5",
}

def codificar(texto):
    codificacao = ""
    for caracter in texto:
        if caracter in dicionario:
            codificacao = dicionario[caracter] + codificacao
        else:
            codificacao = caracter + codificacao
    
    return codificacao

def contarModificacoes(texto):
    qnt_modificacoes = 0    
    for caracter in dicionario:
        qnt_modificacoes += texto.count(caracter)
    
    return qnt_modificacoes


def temNumero(entrada):
    resultado = False

    for caracter in entrada:
        if caracter.isdigit():
            resultado = True
            break
    
    return resultado

def ehVazia(entrada):
    if entrada == "":
        return True
    else:
        return False


if __name__ == "__main__":
    entrada = input()

    if ehVazia(entrada):
        print("vazia")
        print("0")
    
    elif temNumero(entrada):
        print("numeros")
        print("0")
    
    else:
        codificacao = codificar(entrada)
        qnt_modificacoes = contarModificacoes(entrada)

        print(codificacao)
        print(qnt_modificacoes)