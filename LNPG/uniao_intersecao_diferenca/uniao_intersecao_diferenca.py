vetor1 = []
vetor2 = []

n1 = int(input())
n2 = int(input())

for n in range(n1):
    vetor1.append(input())

for n in range(n2):
    vetor2.append(input())

uniao = list(dict.fromkeys(vetor2 + vetor1))
intersecao = [n for n in vetor1 if n in vetor2]
diferenca = [n for n in vetor1 if not(n in intersecao)]

print(uniao, intersecao, diferenca, sep = "\n")