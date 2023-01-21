# https://judge.softuni.org/Contests/Practice/Index/1057#5

while True:
    number = int(input())
    if number < 1 or number > 100:
        print("Invalid input")
    else:
        print(f"The number is: {number}")
        break
