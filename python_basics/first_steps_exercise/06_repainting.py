# https://judge.softuni.org/Contests/Compete/Index/2424#5

nylon_area = int(input())
paint_liters = int(input())
thinner_liters = int(input())
working_hours = int(input())

paint_price = (paint_liters * (1 + 0.10)) * 14.50
nylon_price = (nylon_area + 2) * 1.50
thinner_price = thinner_liters * 5.00
total_matterials = nylon_price + paint_price + thinner_price + 0.40
hour_price = total_matterials * 0.30
total_work = hour_price * working_hours

print(total_work + total_matterials)
