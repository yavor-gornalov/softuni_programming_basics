# https://judge.softuni.org/Contests/Practice/Index/1051#7

# user input
city = input()
trades = float(input())

# logics
is_valid_city = city == "Sofia" or city == "Varna" or city == "Plovdiv"
is_valid_trades = not(trades < 0)
is_valid = is_valid_trades and is_valid_city

commission = 0
if is_valid:
    if city == "Sofia":
        if 0 <= trades <= 500:
            commission = 5
        elif 500 < trades <= 1000:
            commission = 7
        elif 1000 < trades <= 10000:
            commission = 8
        else:
            commission = 12
    elif city == "Varna":
        if 0 <= trades <= 500:
            commission = 4.5
        elif 500 < trades <= 1000:
            commission = 7.5
        elif 1000 < trades <= 10000:
            commission = 10
        else:
            commission = 13
    elif city == "Plovdiv":
        if 0 <= trades <= 500:
            commission = 5.5
        elif 500 < trades <= 1000:
            commission = 8
        elif 1000 < trades <= 10000:
            commission = 12
        else:
            commission = 14.5

    commission = trades * commission / 100
    print(f"{commission:.2f}")

else:
    print("error")
