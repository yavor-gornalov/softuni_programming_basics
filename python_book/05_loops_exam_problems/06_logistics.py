# https://judge.softuni.org/Contests/Practice/Index/1054#5

loads_count = int(input())

bus_price = 200
truck_price = 175
train_price = 120

bus_load = truck_load = train_load = 0
load_total = average_price = 0

for _ in range(1, loads_count + 1):
    load_weight = int(input())
    load_total += load_weight
    if load_weight <= 3:
        average_price += bus_price * load_weight
        bus_load += load_weight
    elif load_weight <= 11:
        average_price += truck_price * load_weight
        truck_load += load_weight
    else:
        average_price += train_price * load_weight
        train_load += load_weight

average_price /= load_total

print(f"{average_price:.2f}")
print(f"{100 * bus_load / load_total:.2f}%")
print(f"{100 * truck_load / load_total:.2f}%")
print(f"{100 * train_load / load_total:.2f}%")
