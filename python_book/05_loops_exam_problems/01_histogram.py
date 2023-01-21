# https://judge.softuni.org/Contests/Practice/Index/1054#0

n = int(input())

p200 = p400 = p600 = p800 = p1000 = 0
for _ in range(1, n + 1):
    number = int(input())
    if number < 200:
        p200 += 1
    elif number < 400:
        p400 += 1
    elif number < 600:
        p600 += 1
    elif number < 800:
        p800 += 1
    else:
        p1000 += 1

print(f"{100 * (p200 / n):.2f}%")
print(f"{100 * (p400 / n):.2f}%")
print(f"{100 * (p600 / n):.2f}%")
print(f"{100 * (p800 / n):.2f}%")
print(f"{100 * (p1000 / n):.2f}%")
