# https://judge.softuni.org/Contests/Practice/Index/1050#4

hours_demanded = int(input())
days_available = int(input())
workers_count = int(input())

hours_per_worker = (1 - 0.10) * days_available * (8 + 2)
total_hours = hours_per_worker * workers_count
hours_balance = int(total_hours - hours_demanded)

if hours_balance >= 0:
    print(f"Yes!{hours_balance} hours left.")
else:
    print(f"Not enough time!{abs(hours_balance)} hours needed.")
