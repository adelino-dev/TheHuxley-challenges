from math import ceil

n = int(input())
resultado_batalhas = []

for batalha in range(n):
    v1, v2, d1, d2 = map(int, input().split())
    
    t2 = ceil(v1/d2) #turnos necess�rios para Bezaliel vencer
    vencedor = "Bezaliel"

    t = 0
    while t2 > 0:
        t1 = ceil(v2/d1) #turnos necess�rios para Clodes vencer
        if t1 <= t2:
            vencedor = "Clodes"
            break
        else:
            d1 += 50
            t += 1
        t2 -= 1
        t1 = ceil(v2/d1)+t

    resultado_batalhas.append(vencedor)

for vencedor in resultado_batalhas:
    print(vencedor)