# https://judge.softuni.org/Contests/Practice/Index/1654#5

total_days = int(input())
hours_per_day = int(input())

total_tax = 0
for current_day in range(1, total_days + 1):
    daily_tax = 0
    for hour in range(1, hours_per_day + 1):
        hour_cost = 1
        if current_day % 2 == 0 and hour % 2 != 0:
            hour_cost = 2.50
        if current_day % 2 != 0 and hour % 2 == 0:
            hour_cost = 1.25

        daily_tax += hour_cost

    total_tax += daily_tax
    print(f"Day: {current_day} - {daily_tax:.2f} leva")

print(f"Total: {total_tax:.2f} leva")
