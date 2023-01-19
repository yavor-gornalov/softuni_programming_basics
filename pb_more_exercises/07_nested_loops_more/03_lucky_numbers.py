# https://judge.softuni.org/Contests/Practice/Index/1381#2

happy_number = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for m in range(1, 10):
                if happy_number % (i + j) == 0 and (i + j) == (k + m):
                    print(f"{i}{j}{k}{m}", end=" ")
