year = int(input())
if (year%100 == 0 and year%400 != 0):
    print("Nao bissexto")
elif year%4 ==0:
    print("Bissexto")
else:
    print("Nao bissexto")