hall_rent = int(input())

cake_price = 0.20 * hall_rent
drinks = (1 - 0.45) * cake_price
animator = hall_rent / 3

total_cost = hall_rent + cake_price + drinks + animator

print(total_cost)
