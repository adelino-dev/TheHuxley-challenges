nacionality = input()
occupation = input()
weaponsQuantity = int(input())
caliber = int(input())

if nacionality == "E":
    if weaponsQuantity == 0:
        print("Liberado")
    else:
        print("Barrado")

else:
    if occupation == "M":
        print("Liberado")
    
    elif occupation =="C" and weaponsQuantity<=2 and caliber<=38:
        print("Liberado")

    elif occupation in ["T","O"] and weaponsQuantity<=1 and caliber <=22:
        print("Liberado")
    
    else:
        print("Barrado")