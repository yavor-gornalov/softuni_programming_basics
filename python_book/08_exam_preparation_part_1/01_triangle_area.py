# https://judge.softuni.org/Contests/Practice/Index/1059#0

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

side = max(x2, x3) - min(x2, x3)
height = max(y1, y2) - min(y1, y2)

triangle_area = (side * height) / 2

print(triangle_area)
