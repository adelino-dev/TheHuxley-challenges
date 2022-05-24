days = int(input())
kilometers = int(input())

total = 30*days + kilometers*0.01
total = total -(total*0.1)

print("%.2f" % total)