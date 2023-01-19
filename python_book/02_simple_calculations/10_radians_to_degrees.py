# https://judge.softuni.org/Contests/Practice/Index/1047#9

from math import pi
# Angle in Radians × 180°/π = Angle in Degrees
radians = float(input())
degrees = round((180 * radians) / pi)

print(degrees)
