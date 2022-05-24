kwh = float(input())

price = kwh*1.50
discount = (price*(15/100))
discount_price = price - discount

print("Valor a ser pago: R$ %.2f reais" % price)
print("Valor a ser pago com desconto: R$ %.2f reais" % discount_price)