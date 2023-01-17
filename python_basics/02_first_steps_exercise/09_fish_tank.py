# https://judge.softuni.org/Contests/Compete/Index/2424#8

length = int(input())
weight = int(input())
height = int(input())
percent = float(input())

total_volume = length * weight * height / 1000
water_volume = total_volume * (100 - percent) / 100

print(water_volume)
