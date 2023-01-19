# https://judge.softuni.org/Contests/Practice/Index/1654#4

n = int(input())

mod_2 = mod_3 = mod_4 = 0
for _ in range(n):
    number = int(input())

    if number % 2 == 0:
        mod_2 += 1
        if number % 4 == 0:
            mod_4 += 1

    if number % 3 == 0:
        mod_3 += 1

mod_2_percent = 0
if mod_2 > 0:
    mod_2_percent = 100 * mod_2 / n

mod_3_percent = 0
if mod_3 > 0:
    mod_3_percent = 100 * mod_3 / n

mod_4_percent = 0
if mod_4 > 0:
    mod_4_percent = 100 * mod_4 / n

print(f"{mod_2_percent:.2f}%\n"
      f"{mod_3_percent:.2f}%\n"
      f"{mod_4_percent:.2f}%")
