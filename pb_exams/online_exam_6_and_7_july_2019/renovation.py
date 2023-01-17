from math import ceil

wall_height = int(input())
wall_width = int(input())
unpainted_walls_percent = int(input())

total_area = 4 * wall_width * wall_height
painted_area = ceil(((100 - unpainted_walls_percent) * total_area) / 100)

paint_liters = input()
while paint_liters != "Tired!":
    paint_liters = int(paint_liters)
    painted_area -= paint_liters

    if painted_area <= 0:
        break

    paint_liters = input()

if painted_area > 0:
    print(f"{painted_area} quadratic m left.")
elif painted_area < 0:
    print(f"All walls are painted and you have {abs(painted_area)} l paint left!")
else:
    print(f"All walls are painted! Great job, Pesho!")
