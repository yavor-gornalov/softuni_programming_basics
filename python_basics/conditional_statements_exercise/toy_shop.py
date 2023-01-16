# user input
trip_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

# logic
puzzle_total = 2.60 * puzzle_count
doll_total = 3 * doll_count
bear_total = 4.10 * bear_count
minion_total = 8.20 * minion_count
truck_total = 2 * truck_count

total_count = puzzle_count + doll_count + bear_count + minion_count + truck_count
total_sum = puzzle_total + doll_total + bear_total + minion_total + truck_total

if total_count >= 50:
    total_sum -= 0.25 * total_sum

trip_sum = (1 - 0.10) * total_sum

# console output
if trip_sum >= trip_price:
    print(f"Yes! {trip_sum - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - trip_sum:.2f} lv needed.")
