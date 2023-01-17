guests_count = int(input())
envelope_price = float(input())
budget = float(input())

cake_cost = 0.10 * budget

discount = 0
if guests_count < 10:
    pass
elif guests_count <= 15:
    discount = 0.15
elif guests_count <= 20:
    discount = 0.20
else:
    discount = 0.25

envelope_cost = (1 - discount) * envelope_price * guests_count

total_cost = envelope_cost + cake_cost

balance = budget - total_cost

if balance > 0:
    print(f"It is party time! {balance:.2f} leva left.")
else:
    print(f"No party! {abs(balance):.2f} leva needed.")
