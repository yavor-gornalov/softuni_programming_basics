# user input
budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

# logics
gpu_price = 250.00
gpu_total = gpu_price * gpu_count
cpu_price = 0.35 * gpu_total
cpu_total = cpu_price * cpu_count
ram_price = 0.10 * gpu_total
ram_total = ram_price * ram_count

total_sum = gpu_total + cpu_total + ram_total

if gpu_count > cpu_count:
    total_sum -= 0.15 * total_sum

# console output
if budget < total_sum:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva more!")
else:
    print(f"You have {budget - total_sum:.2f} leva left!")
