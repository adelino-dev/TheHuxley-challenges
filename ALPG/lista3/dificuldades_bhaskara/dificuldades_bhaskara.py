from math import sqrt, pow

n = int(input())
equacoes = []
variaveis = []

for i in range(n):
    equacao = input()
    ax, bx, c = equacao.split(" + ")
    a = (ax.split("x"))[0] 
    b= (bx.split("x"))[0]

    valoresSeparados = [int(i) for i in [a, b, c, i+1]]
    variaveis.append(valoresSeparados)
    equacoes.append(equacao)


for i in range(len(equacoes)):
    equacao = equacoes[i]
    a, b, c, i = variaveis[i]
    delta = pow(b, 2) -4*a*c

    print("\nTest %i: %s" % (int(i), equacao))

    if delta > 0:
        x1 = (-b + sqrt(delta))/(2*a)
        x2 = (-b - sqrt(delta))/(2*a)
        print("X1 = {:.2f}".format(x1))
        print("X2 = {:.2f}".format(x2))

    elif delta == 0:
        x = -b/(2*a)
        print("X = {:.2f}".format(x))

    elif delta < 0:
        print("SEM RESPOSTA")
