n, e = map(int, input().split())
extravagancias = [int(i) for i in input().split()]
resultado = "NAO"

for g1 in extravagancias:
    for g2 in extravagancias:
        if g1+g2 == e and g1 !=g2:
            resultado = "SIM"
            break
    if resultado =="SIM":
        break

print(resultado)