mercadorias = {}
resultados = []

#Registrando estoque Inicial:
entrada = input()
while entrada != "9999":
    codigo, quantidade = [int(i) for i in entrada.split()]
    mercadorias[codigo] = quantidade
    entrada = input()


# Registrando pedidos dos clientes
entrada = input()
while entrada != "9999":
    cliente, codigo, quantidade = [int(i) for i in entrada.split()]

    if  mercadorias[codigo] >= quantidade:
        resultados.append("OK")
        mercadorias[codigo] -= quantidade
        
    else:
        resultados.append("ESTOQUE INSUFICIENTE")

    entrada = input()

for resultado in resultados:
    print(resultado)

for codigo in mercadorias:
    quantidade = mercadorias[codigo]
    print(codigo, quantidade)