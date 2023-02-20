# https://judge.softuni.org/Contests/Compete/Index/3880#0

fats_percent = int(input()) / 100
proteins_percent = int(input()) / 100
carbons_percent = int(input()) / 100
total_calories = int(input())
water_percent = int(input()) / 100

FAT_CALORIES = 9
PROTEIN_CALORIES = 4
CARBONS_CALORIES = 4

fat_grams = (fats_percent * total_calories) / FAT_CALORIES
protein_grams = (proteins_percent * total_calories) / PROTEIN_CALORIES
carbon_grams = (carbons_percent * total_calories) / CARBONS_CALORIES

food_total_weight = fat_grams + protein_grams + carbon_grams

food_calories = total_calories / food_total_weight if food_total_weight > 0 else 0

calories_wth_water = (1 - water_percent) * food_calories

print(f"{calories_wth_water:.4f}")
