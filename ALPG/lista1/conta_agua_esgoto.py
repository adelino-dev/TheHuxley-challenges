entrada = input().split()

agua_consumida = float(entrada[0]) #em m3 = 1000l
custo_litroAgua = float(entrada[1]) #em R$

valor_agua = (agua_consumida*1000)*custo_litroAgua
valor_esgoto = valor_agua*(0.8)
valor_total = valor_agua + valor_esgoto

print("%.2f" % valor_agua)
print("%.2f" % valor_esgoto)