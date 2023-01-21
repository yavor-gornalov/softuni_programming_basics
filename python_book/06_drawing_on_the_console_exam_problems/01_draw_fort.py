# https://judge.softuni.org/Contests/Practice/Index/1056#0

n = int(input())

col_size = n // 2
mid_size = 2 * n - 2 * col_size - 4
# mid_size = n - col_size % 2 - 4
fort_width = 2 * col_size + mid_size + 4


# fort top
print(f"/{'^' * col_size}\\{'_'* mid_size}/{'^' * col_size}\\")

# fort body
for i in range(n - 3):
    for j in range(fort_width):
        if j == 0 or j == fort_width - 1:
            print("|", end="")
        else:
            print(" ", end="")
    print()
print(f"|{' ' * (col_size + 1)}{'_'* mid_size}{' ' * (col_size + 1)}|")

# fort base
print(f"\\{'_' * col_size}/{' '* mid_size}\\{'_' * col_size}/")
