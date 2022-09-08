def getFaixaEtaria(idade):
    if idade < 0:
        return "Você ainda não nasceu."

    if idade >= 1 and idade <= 11:
        return "Você é uma criança."

    elif idade >= 12 and idade <= 17:
        return "Você é um adolescente."
    
    elif idade >= 18 and idade <= 35:
        return "Você é um jovem."
    
    elif idade >= 36 and idade <= 64:
        return "Você é um adulto."
    
    else:
        return "Você é um idoso."

if __name__ == "__main__":
    
    idades = []

    while True:
        idade = int(input())
        if idade == 0:
            break
        else:
            idades.append(idade)

    for idade in idades:
        faixaEtaria = getFaixaEtaria(idade)
        print(faixaEtaria)