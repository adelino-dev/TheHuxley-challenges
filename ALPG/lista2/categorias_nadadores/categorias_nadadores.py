age = int(input())

if age>=5 and age<=7:
    print("Infantil A")

elif age>=8 and age<=10:
    print("Infantil B")

elif age>=11 and age<=13:
    print("Juvenil A")

elif age>=14 and age<=17:
    print("Juvenil B")

elif age>=18 and age<=40:
    print("Adulto")

elif age>=41:
    print("Master")

else:
    print("Idade invalida.")