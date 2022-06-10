gallonValue_dollar_eua = float(input()) #3,8 L in EUA
gasolineValue_reais_br =  float(input()) # 1L in BR
dollarQuote = float(input()) #R$


gasolineValue_dollar_eua = gallonValue_dollar_eua/3.8 # 1L in EUA
gasolineValue_reais_eua = gasolineValue_dollar_eua*dollarQuote #1L in EUA

print("Gasolina EUA: R$ %.2f" % gasolineValue_reais_eua)
print("Gasolina Brasil: R$ %.2f" % gasolineValue_reais_br)

if gasolineValue_reais_br> gasolineValue_reais_eua:
    print("Mais barata nos EUA")

elif gasolineValue_reais_br < gasolineValue_reais_eua:
    print("Mais barata no Brasil")

else:
    print("Igual")