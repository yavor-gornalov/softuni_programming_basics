lili_age = int(input())
machine_price = float(input())
toy_price = int(input())

money_total = 0

for age in range(1, lili_age + 1):
    if age % 2 == 0:
        money_total += age // 2 * 10 - 1
    else:
        money_total += toy_price

balance = money_total - machine_price

if balance >= 0:
    print(f"Yes! {balance:.2f}")
else:
    print(f"No! {abs(balance):.2f}")
