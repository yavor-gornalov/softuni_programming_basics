# https://judge.softuni.org/Contests/Practice/Index/1745#3

city = input()
pack_type = input()
is_vip = input()
days_count = int(input())

error_flag = False

if days_count < 1:
    print("Days must be positive number!")
    error_flag = True

price_per_day = 0
discount = 0
if city == "Bansko" or city == "Borovets":
    if pack_type == "withEquipment":
        price_per_day = 100
        discount = 0.10
    elif pack_type == "noEquipment":
        price_per_day = 80
        discount = 0.05
    else:
        print("Invalid input!")
        error_flag = True

elif city == "Varna" or city == "Burgas":
    if pack_type == "withBreakfast":
        price_per_day = 130
        discount = 0.12
    elif pack_type == "noBreakfast":
        price_per_day = 100
        discount = 0.07
    else:
        print("Invalid input!")
        error_flag = True
else:
    print("Invalid input!")
    error_flag = True

if is_vip == "no":
    discount *= 0
elif is_vip == "yes":
    pass
else:
    print("Invalid input!")
    error_flag = True

if days_count > 7:
    days_count -= 1

total = price_per_day * days_count
total -= discount * total

if not error_flag:
    print(f"The price is {total:.2f}lv! Have a nice time!")
