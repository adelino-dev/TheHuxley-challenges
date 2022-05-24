media, num_aulas, faltas = [float(num) for num in (input().split())]

frequencia = ((num_aulas-faltas)/num_aulas)*100 #em %

if frequencia >= 75 and media >=5:
    print("APROVADO")
elif frequencia >= 50 and media >=7:
    print("APROVADO")
else:
    print("REPROVADO")