from math import pi

figure = input()

area = 0

if figure == 'square':
    a = float(input())
    area = a * a
elif figure == 'rectangle':
    a, b = float(input()), float(input())
    area = a * b
elif figure == 'circle':
    r = float(input())
    area = pi * r ** 2
elif figure == 'triangle':
    a, h = float(input()), float(input())
    area = (a * h) / 2

print(f"{area:.3f}")
