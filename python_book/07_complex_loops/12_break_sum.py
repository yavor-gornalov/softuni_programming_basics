# https://judge.softuni.org/Contests/Practice/Index/1057#11

has_finished = False
for i in range(1, 4):
    for j in range(3, 0, -1):
        if i + j == 2:
            has_finished = True
            break
        print(i, j)
    if has_finished:
        break
