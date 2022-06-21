qntImas = int(input())

groups = 1
biggest = 0

m = int(input()) #orientação do ímã: 10 --> N p/ esquerda; 01 --> N p/ direita
grupo = [m]

for i in range(qntImas-1):
    m = int(input())
    if m == grupo[0]:
        grupo.append(m)

    else:
        groups +=1
        qntImas = len(grupo)

        if qntImas > biggest:
            biggest = qntImas
        grupo = [m]

print("groups: %i, biggest: %i" % (groups, biggest))
