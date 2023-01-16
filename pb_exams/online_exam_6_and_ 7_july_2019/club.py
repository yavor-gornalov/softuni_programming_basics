profit_demanded = float(input())

order_total = 0
while order_total < profit_demanded:
    cocktail = input()
    if cocktail == "Party!":
        break
    count = int(input())
    price = len(cocktail)

    order_sum = price * count

    if order_sum % 2 != 0:
        order_sum -= 0.25 * order_sum

    order_total += order_sum

balance = order_total - profit_demanded

if balance < 0:
    print(f"We need {abs(balance):.2f} leva more.")
else:
    print("Target acquired.")

print(f"Club income - {order_total:.2f} leva.")
