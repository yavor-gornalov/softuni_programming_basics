# https://judge.softuni.org/Contests/Practice/Index/1637#8

eggs_count = int(input())

max_colour = ''
max_count = -1
red, orange, blue, green = 0, 0, 0, 0
for _ in range(eggs_count):
    egg_colour = input()
    if egg_colour == "red":
        red += 1
    elif egg_colour == "orange":
        orange += 1
    elif egg_colour == "blue":
        blue += 1
    elif egg_colour == "green":
        green += 1

    if red > max_count:
        max_count = red
        max_colour = egg_colour
    elif orange > max_count:
        max_count = orange
        max_colour = egg_colour
    elif blue > max_count:
        max_count = blue
        max_colour = egg_colour
    elif green > max_count:
        max_count = green
        max_colour = egg_colour

print(f"Red eggs: {red}\n"
      f"Orange eggs: {orange}\n"
      f"Blue eggs: {blue}\n"
      f"Green eggs: {green}\n"
      f"Max eggs: {max_count} -> {max_colour}")
