chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_holiday = input()

if is_holiday == "Y":
    is_holiday = True
elif is_holiday == "N":
    is_holiday = False

chrysanthemums_price = 2.00
roses_price = 4.10
tulips_price = 2.50
if season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

bouquet_price = chrysanthemums_price * chrysanthemums_count + roses_price * roses_count + tulips_price * tulips_count

if is_holiday:
    bouquet_price += 0.15 * bouquet_price

if tulips_count > 7 and season == "Spring":
    bouquet_price -= 0.05 * bouquet_price

if roses_count >= 10 and season == "Winter":
    bouquet_price -= 0.10 * bouquet_price

if chrysanthemums_count + roses_count + tulips_count > 20:
    bouquet_price -= 0.20 * bouquet_price

bouquet_price += 2

print(f"{bouquet_price:.2f}")
