data_indice = {}
inexistente = "Dados indisponiveis para este periodo"
resultados = []

num_meses = int(input())
for num in range(num_meses):
  data, indice = input().split()
  indice = float(indice.replace(",","."))
  ano, mes = map(int, data.split("-"))

  data_indice[(ano, mes)] = indice


while True:
  entrada = input()
  if entrada == "*":
    break

  entrada = entrada.split()
  if entrada[0] == "M":
    mes, ano = map(int, entrada[1].split('/'))

    if (ano, mes) in data_indice:
      indice = data_indice[(ano, mes)]
      resultado = indice
    else:
      resultado = inexistente
  
  else:
    data = entrada[1]
    num = int(entrada[2])

    mes, ano = map(int, data.split('/'))

    resultado = 0

    while resultado != inexistente and num > 0:
      if mes > 12:
        mes = 1
        ano += 1

      if (ano, mes) in data_indice:
        indice = data_indice[(ano, mes)]
        resultado += indice
        mes += 1
        num -= 1

      else:
        resultado = inexistente

  resultados.append(resultado),

for resultado in resultados:
  if resultado != inexistente:
    print("%.2f" % resultado)
  else:
    print(resultado)