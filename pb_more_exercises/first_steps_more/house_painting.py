x = float(input())
y = float(input())
h = float(input())

window_area = 2 * 1.50 ** 2
door_area = 1.2 * 2
sides_area = 2 * (x ** 2 + x * y)
green_area = sides_area - window_area - door_area

red_area = 2 * ((x * y) + (x * h) / 2)

green_paint_lt = green_area / 3.4
red_paint_lt = red_area / 4.3

print("%.2f" % green_paint_lt)
print("%.2f" % red_paint_lt)
