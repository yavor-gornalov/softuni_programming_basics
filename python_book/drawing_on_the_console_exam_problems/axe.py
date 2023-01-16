n = int(input())

width = 5 * n
left_dashes = 3 * n
middle_dashes = 0
right_dashes = width - left_dashes - middle_dashes - 2

for _ in range(n):
    print(f"{'-' * left_dashes}*{'-' * middle_dashes}*{'-' * right_dashes}")
    middle_dashes += 1
    right_dashes -= 1

middle_dashes -= 1
right_dashes += 1
left_dashes += 1

axe_height = n // 2

for _ in range(axe_height):
    print(f"{'*' * left_dashes}{'-' * middle_dashes}*{'-' * right_dashes}")

left_dashes -= 1
for _ in range(axe_height - 1):
    print(f"{'-' * left_dashes}*{'-' * middle_dashes}*{'-' * right_dashes}")
    middle_dashes += 2
    right_dashes -= 1
    left_dashes -= 1

print(f"{'-' * left_dashes}*{'*' * middle_dashes}*{'-' * right_dashes}")
