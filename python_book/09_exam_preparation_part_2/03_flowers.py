# https://judge.softuni.org/Contests/Practice/Index/1060#2

chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_holiday = input()

increase = 0
if is_holiday == "Y":
    increase = 0.15

chrysanthemums_price = roses_price = tulips_price = 0

if season in ["Spring", "Summer"]:
    chrysanthemums_price = (1 + increase) * 2.00
    roses_price = (1 + increase) * 4.10
    tulips_price = (1 + increase) * 2.50

elif season in ["Autumn", "Winter"]:
    chrysanthemums_price = (1 + increase) * 3.75
    roses_price = (1 + increase) * 4.50
    tulips_price = (1 + increase) * 4.15

bouquet_price = chrysanthemums_price * chrysanthemums_count + roses_price * roses_count + tulips_price * tulips_count

if tulips_count > 7 and season == "Spring":
    bouquet_price -= 0.05 * bouquet_price

if roses_count >= 10 and season == "Winter":
    bouquet_price -= 0.10 * bouquet_price

if chrysanthemums_count + roses_count + tulips_count > 20:
    bouquet_price -= 0.20 * bouquet_price

bouquet_price += 2

print(f"{bouquet_price:.2f}")
