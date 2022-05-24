pi = 3.14
height = float(input())
radius = float(input())

volume = pi*(radius**2) * height
surfaceArea = 2*pi*radius*height + 2*pi*(radius**2)


print(round(volume, 2))
print(round(surfaceArea, 2))