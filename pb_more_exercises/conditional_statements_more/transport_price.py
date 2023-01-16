# user input
distance = int(input())
day_night = input()

# logics
taxi_tariff = 0.79
if day_night == "night":
    taxi_tariff = 0.90

taxi_bill = distance * taxi_tariff + 0.70
bus_bill = distance * 0.09
train_bill = distance * 0.06

if distance < 20:
    cheapest_bill = taxi_bill
elif distance < 100:
    cheapest_bill = min(taxi_bill, bus_bill)
else:
    cheapest_bill = min(taxi_bill, bus_bill, train_bill)

# console output
print(f"{cheapest_bill:.2f}")
