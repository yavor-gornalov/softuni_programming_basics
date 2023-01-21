# https://judge.softuni.org/Contests/Practice/Index/1049#12

from math import pi

figure = input()

area = 0
if figure == "square":
    a = float(input())
    area = a * a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure == "circle":
    r = float(input())
    area = pi * r * r
elif figure == "triangle":
    a = float(input())
    ha = float(input())
    area = a * ha / 2

print(area)
