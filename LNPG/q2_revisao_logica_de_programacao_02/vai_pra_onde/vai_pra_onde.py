cidade = "SEM DESTINO"
km = 0

entrada = input().upper()
while entrada != " " and entrada != "FIM":
    distancia  = int(input())
    passagem = float(input())

    if passagem*2 <= 300.0 and distancia > km:
        cidade = entrada
        km = distancia
    
    entrada = input().upper()

print(cidade)