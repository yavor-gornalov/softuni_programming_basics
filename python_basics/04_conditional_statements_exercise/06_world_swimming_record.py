# https://judge.softuni.org/Contests/Compete/Index/2414#5

from math import floor
record = float(input())
distance = float(input())
speed = float(input())

delay = floor(distance / 15) * 12.5
total_time = distance * speed + delay

if record > total_time:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record:.2f} seconds slower.")
