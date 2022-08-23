def contar(string):
    c = 0
    for i in string:
        c += 1
    return c
    
s = input()
print(contar(s))