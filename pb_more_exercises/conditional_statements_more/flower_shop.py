from math import ceil, floor

# user input
magnolias_count = int(input())  # Магнолии
hyacinths_count = int(input())  # Зюмбюли
roses_count = int(input())  # Рози
cacti_count = int(input())  # Кактуси
gift_price = float(input())

# logics
magnolias_total = 3.25 * magnolias_count
hyacinths_total = 4 * hyacinths_count
roses_total = 3.50 * roses_count
cacti_total = 8 * cacti_count
flowers_total = magnolias_total + hyacinths_total + roses_total + cacti_total
flowers_total -= 0.05 * flowers_total

gift_money = flowers_total - gift_price
is_enough = gift_money >= 0

# console output
if is_enough:
    print(f"She is left with {floor(gift_money)} leva.")
else:
    print(f"She will have to borrow {ceil(abs(gift_money))} leva.")
