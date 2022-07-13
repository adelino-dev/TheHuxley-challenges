n = input()

quantities = 0

for i in range(20):
    x = (input())
    if x == n:
        quantities += 1
    if x == '-1':
        break

print("{} aparece {} vezes".format(n, quantities))