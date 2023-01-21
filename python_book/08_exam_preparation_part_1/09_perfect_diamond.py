# https://judge.softuni.org/Contests/Practice/Index/1059#8

n = int(input())

spaces = n - 1
stars = 0

# top
for _ in range(n):
    print(f"{' ' * spaces}{'*-' * stars}*{' ' * spaces}")
    spaces -= 1
    stars += 1

# bottom
spaces += 2
stars -= 2
for _ in range(n - 1):
    print(f"{' ' * spaces}{'*-' * stars}*{' ' * spaces}")
    spaces += 1
    stars -= 1
