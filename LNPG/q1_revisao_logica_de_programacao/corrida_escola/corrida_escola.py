n, m = input().split()


ganhador = 0
tempos = []

for competidor in range(1, int(n)+1):
    tempo = sum([int(i) for i in input().split()])
    tempos.append(tempo)

    if min(tempos) == tempo:
        ganhador = competidor
    
print(ganhador)

