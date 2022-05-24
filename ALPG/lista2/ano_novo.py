discounts1 = {
    20:(12, 15, 20),
    21:(17, 22, 27),
    22:(20, 22, 30),
    23:(25, 29, 35),
    24:(35, 35, 50)
}

discounts2 = {
    25:(15, 13, 0, 10),
    26:(19, 25, 5, 23),
    27:(24, 30, 12, 33),
    28:(30, 32, 20, 35),
    29:(35, 40, 33, 42),
    30:(35, 40, 33, 42),
    31:(40, 47, 45, 66)
}

def discount(day, foodValue, sodaValue, decorationValue, beerValue=None):
    if day<20:
        sodaValue -= sodaValue*0.1
        decorationValue -= decorationValue*0.15
        
        return [foodValue, sodaValue, decorationValue]
    elif day<25:
        f, s, d = discounts1[day]
        foodValue -= foodValue*(f/100)
        sodaValue -= sodaValue*(s/100)
        decorationValue -= decorationValue*(d/100)
        
        return [foodValue, sodaValue, decorationValue]
    else:
        f, s, b, d = discounts2[day]
        foodValue -= foodValue*(f/100)
        sodaValue -= sodaValue*(s/100)
        beerValue -= beerValue*(b/100)
        decorationValue -= decorationValue*(d/100)

        return [foodValue, sodaValue, beerValue, decorationValue]

if __name__ == "__main__":
    day1 = int(input())
    foodValue1, sodaValue1, decorationValue1 = [float(f) for f in input().split()]

    day2 = int(input())
    foodValue2, sodaValue2, beerValue2, decorationValue2 = [float(f) for f in input().split()]
    

    totalChristmas = sum(discount(day1, foodValue1, sodaValue1, decorationValue1))

    totalNewYear = sum(discount(day2, foodValue2, sodaValue2, decorationValue2, beerValue = beerValue2))

    print("Compras de natal: R$ %.2f." % totalChristmas)
    print("Compras de ano novo: R$ %.2f." % totalNewYear)
    print("Total das compras: R$ %.2f." % (totalChristmas+totalNewYear))