level = int(input())
if 1<=level and level<=20:
    potencia =  20+(level)**3

elif 21<=level and level<=40:
    potencia =  8000+(level-10)**2

elif 41<=level and level<=60:
    potencia =  9000+5*level

elif 61<=level and level<=80:
    potencia =  9300+2*level

else:
    potencia = 9500 + level

print("Potencia de : %i W" % potencia)