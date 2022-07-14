n, d = input().split()

numbersDrawn = []

for i in range(int(n)):
    number = input()
    if number[-1] == d:
        numbersDrawn.append(int(number))

difference = 5 -len(numbersDrawn)
if difference >0:
    for i in range(difference):
        numbersDrawn.append(-1)

numbersDrawn.sort()
for number in numbersDrawn[-5:]:
    print(number)