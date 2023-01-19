# https://judge.softuni.org/Contests/Practice/Index/1047#11

amount = float(input())
currency_from = input()
currency_to = input()

coefficient_from = 0
if currency_from == "BGN":
    coefficient_from = 1
elif currency_from == "USD":
    coefficient_from = 1.79549
elif currency_from == "EUR":
    coefficient_from = 1.95583
elif currency_from == "GBP":
    coefficient_from = 2.53405

amount_from = coefficient_from * amount

coefficient_to = 0
if currency_to == "BGN":
    coefficient_to = 1
elif currency_to == "USD":
    coefficient_to = 1 / 1.79549
elif currency_to == "EUR":
    coefficient_to = 1 / 1.95583
elif currency_to == "GBP":
    coefficient_to = 1 / 2.53405

amount_to = coefficient_to * amount_from

print(f"{amount_to:.2f} {currency_to}")
