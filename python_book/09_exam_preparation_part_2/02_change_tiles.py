# https://judge.softuni.org/Contests/Practice/Index/1060#1

from math import ceil

budget = float(input())
floor_width = float(input())
floor_length = float(input())
tile_side = float(input())
tile_height = float(input())
tile_price = float(input())
worker_price = float(input())

floor_area = floor_length * floor_width

tile_area = (tile_side * tile_height) / 2

total_tiles = 5
if tile_area > 0:
    total_tiles += ceil(floor_area / tile_area)

total_price = total_tiles * tile_price + worker_price

balance = budget - total_price

if balance >= 0:
    print(f"{balance:.2f} lv left.")
else:
    print(f"You'll need {abs(balance):.2f} lv more.")
