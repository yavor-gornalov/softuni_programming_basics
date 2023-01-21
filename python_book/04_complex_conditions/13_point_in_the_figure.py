# https://judge.softuni.org/Contests/Practice/Index/1051#12

h = int(input())
x = int(input())
y = int(input())

in_horizontal_figure = 0 < x < 3 * h and 0 < y < h
in_vertical_figure = h < x < 2 * h and h <= y < 4 * h

out_horizontal_figure = x < 0 or x > 3 * h or y < 0 or y > h
out_vertical_figure = x < h or x > 2 * h or y < h or y > 4 * h

if in_horizontal_figure or in_vertical_figure:
    print("inside")
elif out_horizontal_figure and out_vertical_figure:
    print("outside")
else:
    print("border")
