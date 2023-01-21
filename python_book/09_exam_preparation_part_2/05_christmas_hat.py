# https://judge.softuni.org/Contests/Practice/Index/1060#4

n = int(input())

# top
print(f"{'.' * (2 * n - 1)}/|\\{'.' * (2 * n - 1)}")
print(f"{'.' * (2 * n - 1)}\\|/{'.' * (2 * n - 1)}")

# middle
dots = 2 * n - 1
dashes = 0
for rows in range(2 * n):
    print(f"{'.' * dots}*{'-' * dashes}*{'-' * dashes}*{'.' * dots}")
    dots -= 1
    dashes += 1

# bottom
print(f"{'*' * (4 * n + 1)}")
print(f"{'*.' * 2 * n}*")
print(f"{'*' * (4 * n + 1)}")
