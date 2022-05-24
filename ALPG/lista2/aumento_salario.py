salary = float(input())
if salary <= 280:
    increase = salary*0.2

elif 280<salary and salary<700:
    increase = salary*0.15

elif 700<=salary and salary<1500:
    increase = salary*0.1
    
else:
    increase = salary*0.05

print(salary+increase)