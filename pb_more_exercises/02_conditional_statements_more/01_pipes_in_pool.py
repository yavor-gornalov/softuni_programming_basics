# https://judge.softuni.org/Contests/Practice/Index/1658#0

# user input
volume = int(input())
first_flow = int(input())
second_flow = int(input())
absence_time = float(input())

# logics
first_total = first_flow * absence_time
second_total = second_flow * absence_time
water_total = first_total + second_total

first_percent = 100 * (first_total / water_total)
second_percent = 100 * (second_total / water_total)

# console output
if volume >= water_total:
    volume_percent = 100 * (water_total / volume)
    print(f"The pool is {volume_percent:.2f}% full. Pipe 1: {first_percent:.2f}%. Pipe 2: {second_percent:.2f}%.")
else:
    print(f"For {absence_time} hours the pool overflows with {water_total - volume:.2f} liters.")
