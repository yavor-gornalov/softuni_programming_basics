# https://judge.softuni.org/Contests/Practice/Index/1056#4

# https://judge.softuni.org/Contests/Practice/Index/1056#3

n = int(input())

# top
outer_dots = (n - 1) // 2
inner_dots = n - 2
for i in range(n - 1):
    if i == 0:
        ch = '#'
    else:
        ch = '.'
    print(f"{'.' * outer_dots}#{ch * inner_dots}#{'.' * outer_dots}")

# middle
print(f"{'#' * outer_dots}#{'.' * inner_dots}#{'#' * outer_dots}")

# bottom
outer_dots = 1
inner_dots = 2 * n - 5
while inner_dots > 0:
    print(f"{'.' * outer_dots}#{'.' * inner_dots}#{'.' * outer_dots}")
    outer_dots += 1
    inner_dots -= 2
else:
    print(f"{'.' * outer_dots}#{'.' * outer_dots}")

