fruit = input()
pack_size = input()
packs_count = int(input())

pack_price = 0
if fruit == "Watermelon":
    if pack_size == "small":
        pack_price = 2 * 56
    elif pack_size == "big":
        pack_price = 5 * 28.70
elif fruit == "Mango":
    if pack_size == "small":
        pack_price = 2 * 36.66
    elif pack_size == "big":
        pack_price = 5 * 19.60
elif fruit == "Pineapple":
    if pack_size == "small":
        pack_price = 2 * 42.10
    elif pack_size == "big":
        pack_price = 5 * 24.80
elif fruit == "Raspberry":
    if pack_size == "small":
        pack_price = 2 * 20
    elif pack_size == "big":
        pack_price = 5 * 15.20

total_price = pack_price * packs_count

if total_price < 400:
    pass
elif total_price <= 1000:
    total_price -= 0.15 * total_price
else:
    total_price -= 0.5 * total_price

print(f"{total_price:.2f} lv.")
