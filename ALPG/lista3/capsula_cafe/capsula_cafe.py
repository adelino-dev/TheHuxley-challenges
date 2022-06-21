capsulas = 0
for i in range(7):
    quantidade = int(input())
    tipo = input().upper()

    if tipo == "P":
        capsulas += quantidade*10

    else:
        capsulas += quantidade*16 

xicaras= capsulas*2

print(capsulas)
print(xicaras//7)