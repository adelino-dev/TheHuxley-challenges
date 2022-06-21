resultados = []
while True:
    a, b = map(int, input().split())
    if b > 0:
        intervalo = map(str, range(a, b+1))
        intervalo = "".join(intervalo)

        resultado = [str(intervalo.count(str(i))) for i in range(10)]
        resultados.append(resultado)
    else:
        break
for resultado in resultados:
    print(" ".join(resultado))