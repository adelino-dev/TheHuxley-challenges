a = int(input())
b = int(input())
c = int(input())

if a != b and b == c:
    print("A")

elif b != a and a == c:
    print("B")

elif c != a and a == b:
    print("C")

else:
    print("*")