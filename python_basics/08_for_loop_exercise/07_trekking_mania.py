# https://judge.softuni.org/Contests/Compete/Index/2418#6

groups_count = int(input())

musala_climbers = 0
monblan_climbers = 0
kilimandjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

for _ in range(1, groups_count + 1):
    climbers_count = int(input())
    if climbers_count <= 5:
        musala_climbers += climbers_count
    elif climbers_count <= 12:
        monblan_climbers += climbers_count
    elif climbers_count <= 25:
        kilimandjaro_climbers += climbers_count
    elif climbers_count <= 40:
        k2_climbers += climbers_count
    else:
        everest_climbers += climbers_count

total_climbers = musala_climbers + monblan_climbers + kilimandjaro_climbers + k2_climbers + everest_climbers
print(f"{100 * musala_climbers / total_climbers:.2f}%")
print(f"{100 * monblan_climbers / total_climbers:.2f}%")
print(f"{100 * kilimandjaro_climbers / total_climbers:.2f}%")
print(f"{100 * k2_climbers / total_climbers:.2f}%")
print(f"{100 * everest_climbers / total_climbers:.2f}%")
