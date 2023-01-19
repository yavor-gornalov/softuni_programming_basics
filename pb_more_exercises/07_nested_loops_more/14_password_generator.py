# https://judge.softuni.org/Contests/Practice/Index/1381#13

num = int(input())
let = int(input())

for a in range(1, num):
    for b in range(1, num):
        for c in range(let):
            for d in range(let):
                for e in range(1, num + 1):
                    if e > a and e > b:
                        print(f"{a}{b}{chr(c + ord('a'))}{chr(d + ord('a'))}{e}", end=" ")
