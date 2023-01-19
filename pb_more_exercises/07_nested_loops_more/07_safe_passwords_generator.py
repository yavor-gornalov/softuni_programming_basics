# https://judge.softuni.org/Contests/Practice/Index/1381#6

limit_x = int(input())
limit_y = int(input())
password_count = int(input())

pass_generated = 0
flag = False
while True:
    a = 35
    b = 64
    for x in range(1, limit_x + 1):
        for y in range(1, limit_y + 1):
            print(f"{chr(a)}{chr(b)}{x}{y}{chr(b)}{chr(a)}", end="|")
            a += 1
            b += 1
            if a > 55:
                a = 35
            if b > 96:
                b = 64
            pass_generated += 1
            if (x == limit_x and y == limit_y) or pass_generated == password_count:
                flag = True
                break

        if flag:
            break
    if flag:
        break
