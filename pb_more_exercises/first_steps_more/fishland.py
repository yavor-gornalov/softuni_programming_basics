mackerel_price = float(input())  # скумрия
sprinkle_price = float(input())  # цаца
bonito_amount = float(input())  # паламуд
safrid_amount = float(input())  # сафрид
mussels_amount = int(input())  # миди

bonito_price = (1 + 0.60) * mackerel_price
safrid_price = (1 + 0.80) * sprinkle_price
mussels_price = 7.50

safrid_total = safrid_price * safrid_amount
bonito_total = bonito_price * bonito_amount
mussels_total = mussels_price * mussels_amount

all_costs = safrid_total + bonito_total + mussels_total

print("%.2f" % all_costs)
