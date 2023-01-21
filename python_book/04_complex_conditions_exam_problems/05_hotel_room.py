# https://judge.softuni.org/Contests/Practice/Index/1052#4

month = input()
nights = int(input())

apartment_price = 0
studio_price = 0
room = ''
if month == "May" or month == "October":
    apartment_price = 65
    studio_price = 50
    if nights > 14:
        apartment_price -= 0.10 * apartment_price
        studio_price -= 0.30 * studio_price
    elif nights > 7:
        studio_price -= 0.05 * studio_price


elif month == "June" or month == "September":
    apartment_price = 68.70
    studio_price = 75.20
    if nights > 14:
        apartment_price -= 0.10 * apartment_price
        studio_price -= 0.20 * studio_price

elif month == "July" or month == "August":
    apartment_price = 77
    studio_price = 76
    if nights > 14:
        apartment_price -= 0.10 * apartment_price

print(f"Apartment: {apartment_price * nights:.2f} lv.")
print(f"Studio: {studio_price * nights:.2f} lv.")
