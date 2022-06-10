year = int(input())
if (year%100 == 0 and year%400 != 0):
    print("NAOBISSEXTO")
elif year%4 ==0:
    print("BISSEXTO")
else:
    print("NAOBISSEXTO")