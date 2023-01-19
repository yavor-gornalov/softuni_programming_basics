# https://judge.softuni.org/Contests/Practice/Index/1680#6

capacity = int(input())
fans_count = int(input())

sector_a = sector_b = sector_v = sector_g = 0
for _ in range(1, fans_count + 1):
    sector = input()
    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

print(f"{100 * sector_a / fans_count:.2f}%")
print(f"{100 * sector_b / fans_count:.2f}%")
print(f"{100 * sector_v / fans_count:.2f}%")
print(f"{100 * sector_g / fans_count:.2f}%")
print(f"{100 * fans_count / capacity:.2f}%")
