sex = input()
time = float(input())
salary = float(input())

if sex == "h" and time>15:
    bonus = salary*0.2

elif sex == "m" and time>10:
    bonus = salary*0.25
else:
    bonus = 200.0

total = salary+bonus
print("%.2f" % total)