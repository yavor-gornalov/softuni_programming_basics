# https://judge.softuni.org/Contests/Practice/Index/2507#1

bag_over_20_price = float(input())
bag_weight = float(input())
days_to_travel = int(input())
bags_count = int(input())

current_bag_price = 0
if bag_weight < 10:
    current_bag_price = 0.20 * bag_over_20_price
elif bag_weight <= 20:
    current_bag_price = 0.50 * bag_over_20_price
else:
    current_bag_price = 1.00 * bag_over_20_price

if days_to_travel < 7:
    current_bag_price += 0.40 * current_bag_price
elif days_to_travel <= 30:
    current_bag_price += 0.15 * current_bag_price
else:
    current_bag_price += 0.10 * current_bag_price

total_bag_price = bags_count * current_bag_price

print((f"The total price of bags is: {total_bag_price:.2f} lv."))
