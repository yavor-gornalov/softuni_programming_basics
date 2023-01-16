season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

discount = 0
if students_count >= 50:
    discount = 0.50
elif students_count >= 20:
    discount = 0.15
elif students_count >= 10:
    discount = 0.05

night_price = 0
if season == "Winter":
    night_price = 9.60
    if group_type == "mixed":
        night_price = 10.00
elif season == "Spring":
    night_price = 7.20
    if group_type == "mixed":
        night_price = 9.50
elif season == "Summer":
    night_price = 15.00
    if group_type == "mixed":
        night_price = 20.00

total_price = students_count * nights_count * night_price
total_price -= discount * total_price

sport = ''
if group_type == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    elif season == "Summer":
        sport = "Volleyball"
elif group_type == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    elif season == "Summer":
        sport = "Football"
elif group_type == "mixed":
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    elif season == "Summer":
        sport = "Swimming"

print(f"{sport} {total_price:.2f} lv.")
