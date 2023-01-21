# https://judge.softuni.org/Contests/Practice/Index/1057#10

while True:
    try:
        print("Enter even number: ", end="")
        n = int(input())
        if n % 2 == 0:
            print(f"Even number entered: {n}")
            break
    except ValueError:
        print("Invalid number.")
