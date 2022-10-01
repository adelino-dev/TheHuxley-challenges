ano_atual = 2152

def contarDigitos(ano):
    return len(str(ano))

def ehBissexto(ano):
    condicao1 = ano %4 == 0
    condicao2 = ano%100 != 0
    condicao3 = ano%400 == 0

    if  condicao1 and (condicao2 or condicao3):
        return True
    else:
        return False

def mensagem(ano):
    if contarDigitos(ano) != 4:
        return "Ano invalido"

    else:
        eh_bissexto = ehBissexto(ano)

        if eh_bissexto and ano == ano_atual:
            texto = "O ano %s eh bissexto" % str(ano)

        elif eh_bissexto and ano < ano_atual:
            texto = "O ano %s foi bissexto" % str(ano)
        
        elif eh_bissexto and ano > ano_atual:
            texto = "O ano %s serah bissexto" % str(ano)

        else:
            texto = "O ano %s NAO eh bissexto" % str(ano)
    
    return texto

entradas = []
while True:
    entrada = int(input())
    if entrada == -1:
        break
    else:
        entradas.append(entrada)

for entrada in entradas:
    print(mensagem(entrada))