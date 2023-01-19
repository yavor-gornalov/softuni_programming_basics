# https://judge.softuni.org/Contests/Practice/Index/2275#3

from math import floor

record_time = float(input())
distance = float(input())
speed = float(input())

climbing_time = distance * speed
delay_time = (distance // 50) * 30
total_time = climbing_time + delay_time

if total_time < record_time:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print((f"No! He was {total_time - record_time:.2f} seconds slower."))
