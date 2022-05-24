print("Informe a primeira nota:")
nota1 = float(input())

print("Informe a segunda nota:")
nota2 = float(input())

print("Informe a terceira nota:")
nota3 = float(input())

media = (nota1+nota2+nota3)/3

if media >= 7:
    print("Aprovado com media %.1f" % media)

elif media < 5:
    print("Reprovado com media %.1f" % media)

else:
    print("Recuperacao com media %.1f" % media)