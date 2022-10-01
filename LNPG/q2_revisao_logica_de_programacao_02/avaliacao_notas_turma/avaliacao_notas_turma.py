respostas = {}

def cadastrar_resposta(aluno, resposta):
    respostas[aluno] = resposta

def calcular_nota(aluno, gabarito):
    nota = 0
    for i in range(5):
        resposta = respostas[aluno][i]
        if resposta == gabarito[i]:
            nota += 1
    return nota

def obter_notas(gabarito):
    notas = []
    for aluno in respostas:
        nota = calcular_nota(aluno, gabarito)
        notas.append(nota)
    
    return notas

def calcular_media(notas):
    media = sum(notas)/len(notas)
    return media

def encontrar_maior(notas):
    maior = max(notas)
    return maior

def encontrar_menor(notas):
    menor = min(notas)
    return menor

if __name__ == "__main__":
    
    entrada = input()
    
    while entrada != "*":

        aluno, resposta = entrada.split()
        cadastrar_resposta(aluno, resposta)
        entrada = input()
    
    gabarito = input()
    notas = obter_notas(gabarito)

    media = calcular_media(notas)
    maior = encontrar_maior(notas)
    menor = encontrar_menor(notas)

    print("Maior:", maior)
    print("Menor:", menor)
    print("Media: %.2f" % media)