outputs = []

while True:
    number1 = int(input())

    if number1 == -1:
        break
    
    else:
        integers = [number1]
        for i in range(999):
            number = int(input())
            integers.append(number)
    
    n = int(input())
    k = integers.count(n)
    outputs.append("%i appeared %i times" % (n,k))

for output in outputs:
    print(output)