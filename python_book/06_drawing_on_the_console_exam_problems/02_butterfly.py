# https://judge.softuni.org/Contests/Practice/Index/1056#1

n = int(input())

butterfly_width = 2 * n - 1
butterfly_height = 2 * (n - 2)

half_wing_width = n - 2
half_wing_height = n - 2

# top wings
for i in range(half_wing_height):
    if i % 2 == 0:
        ch = "*"
    else:
        ch = "-"
    print(f"{ch * half_wing_width}\\ /{ch * half_wing_width}")

# body
print(f"{' ' * half_wing_width} @ {' ' * half_wing_width}")

# bottom wing
for i in range(half_wing_height):
    if i % 2 == 0:
        ch = "*"
    else:
        ch = "-"
    print(f"{ch * half_wing_width}/ \\{ch * half_wing_width}")
