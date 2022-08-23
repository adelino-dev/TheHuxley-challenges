while True:
    ph = float(input())

    if ph == -1:
        break

    elif ph < 7:
        print("ACIDA")
    
    elif ph > 7:
        print("BASICA")

    else:
        print("NEUTRA")