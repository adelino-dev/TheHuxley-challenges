gallons = [int(i) for i in input().split()]

for quantity in gallons:
    if quantity ==1:
        print("1 GALÃO -> 3.79 LITROS")
    else:
        liters = quantity*3.7854
        print("%i GALÕES -> %.2f LITROS" % (quantity, liters))
