seconds = int(input())

h = seconds//3600
m = (seconds%3600)//60
s = (seconds%3600)%60

print(h, "h", m, "m", s, "s")