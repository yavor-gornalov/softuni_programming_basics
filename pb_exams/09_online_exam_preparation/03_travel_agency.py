# https://judge.softuni.org/Contests/Practice/Index/1745#3

resort_name = input()
pack_type = input()
has_vip_discount = input()
vacation_days = int(input())

error_flag = False
if vacation_days < 1:
    print("Days must be positive number!")
    exit()

daily_price, vip_discount = 0, 0
if resort_name in ["Bansko", "Borovets"]:
    if pack_type == "withEquipment":
        daily_price, vip_discount = 100, 0.10
    elif pack_type == "noEquipment":
        daily_price, vip_discount = 80, 0.05
    else:
        error_flag = True

elif resort_name in ["Varna", "Burgas"]:
    if pack_type == "withBreakfast":
        daily_price, vip_discount = 130, 0.12
    elif pack_type == "noBreakfast":
        daily_price, vip_discount = 100, 0.07
    else:
        error_flag = True

else:
    error_flag = True

if has_vip_discount == "yes":
    daily_price -= daily_price * vip_discount
elif has_vip_discount == "no":
    pass
else:
    error_flag = True

if not error_flag:
    if vacation_days > 7:
        vacation_days -= 1
    total_cost = vacation_days * daily_price
    print(f"The price is {total_cost:.2f}lv! Have a nice time!")
else:
    print("Invalid input!")
