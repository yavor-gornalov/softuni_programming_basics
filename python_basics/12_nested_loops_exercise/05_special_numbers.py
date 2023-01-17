# https://judge.softuni.org/Contests/Compete/Index/2422#4

num = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for m in range(1, 10):
                is_valid = num % i == 0 and num % j == 0 and num % k == 0 and num % m == 0
                if is_valid:
                    print(f"{i}{j}{k}{m}", end=' ')
