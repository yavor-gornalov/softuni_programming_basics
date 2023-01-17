# https://judge.softuni.org/Contests/Compete/Index/2421#4

while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())

    saved_money = 0
    saved_money_balance = 0
    while True:
        if saved_money_balance >= budget:
            break
        saved_money = float(input())
        saved_money_balance += saved_money

    print(f"Going to {destination}!")
