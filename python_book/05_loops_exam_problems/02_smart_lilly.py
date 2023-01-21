# https://judge.softuni.org/Contests/Practice/Index/1054#1

lilli_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys_count = 0
money_received = 0
for age in range(1, lilli_age + 1):
    if age % 2 != 0:
        toys_count += 1
    else:
        money_received += age // 2 * 10 - 1

money_from_toys = toys_count * toy_price
total_money = money_received + money_from_toys

money_balance = total_money - washing_machine_price
if money_balance >= 0:
    print(f"Yes! {money_balance:.2f}")
else:
    print(f"No! {abs(money_balance):.2f}")
