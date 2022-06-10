scale = input()
temperature = float(input())

if scale == "K" and temperature >= 0.0:
   TC = temperature - 273.15
   TF = (temperature -273.15)*1.8+32
   print("%.2f C" % TC)
   print("%.2f F" % TF)

elif scale == "F" and temperature >= -459.67:
    TC = (temperature-32)/1.8
    TK =(temperature-32)*(5/9)+273.15
    print("%.2f C" % TC)
    print("%.2f K" % TK)
    
elif scale == "C" and temperature >= -273.0:
    TK = temperature + 273.15
    TF = 1.8*temperature + 32
    print("%.2f F" % TF)
    print("%.2f K" % TK)

else:
    print("Valor de temperatura abaixo do minimo")