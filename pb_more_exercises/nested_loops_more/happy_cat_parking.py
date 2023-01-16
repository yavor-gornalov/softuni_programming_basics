days = int(input())
hours = int(input())

total_cost = 0
for d in range(1, days + 1):
    price = 0
    total_daily_price = 0
    for h in range(1, hours + 1):
        if d % 2 == 0 and h % 2 != 0:
            price = 2.50
        elif d % 2 != 0 and h % 2 == 0:
            price = 1.25
        else:
            price = 1.00
        total_daily_price += price

    print(f"Day: {d} - {total_daily_price:.2f} leva")
    total_cost += total_daily_price

print(f"Total: {total_cost:.2f} leva")
