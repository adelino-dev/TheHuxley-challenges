horas = 0
nxh = 0

while True:
    semestre = int(input())

    if semestre<=0 or semestre>10:
        break
        print("Entrou")

    else:
        carga_horaria = int(input())
        nota = int(input())
        situacao = input()

        if not(situacao in ["T", "AD", "DE", "AE", "DD", "DC"]) and carga_horaria in [33, 50, 67, 83]:
            nxh += nota*carga_horaria
            horas += carga_horaria
            

if horas > 0:
    cre = nxh/horas
    print("%.2f" % cre)

else:
    print("entrada invalida")