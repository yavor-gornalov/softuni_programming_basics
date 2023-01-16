joinery_count = int(input())
joinery_type = input()
delivery = input()
error_flag = False

order_total = 0
if joinery_count < 10:
    error_flag = True
else:
    joinery_price = 0
    if joinery_type == "90X130":
        joinery_price = 110
        if joinery_count > 60:
            joinery_price -= 0.08 * joinery_price
        elif joinery_count > 30:
            joinery_price -= 0.05 * joinery_price

    elif joinery_type == "100X150":
        joinery_price = 140
        if joinery_count > 80:
            joinery_price -= 0.10 * joinery_price
        elif joinery_count > 40:
            joinery_price -= 0.06 * joinery_price

    elif joinery_type == "130X180":
        joinery_price = 190
        if joinery_count > 50:
            joinery_price -= 0.12 * joinery_price
        elif joinery_count > 20:
            joinery_price -= 0.07 * joinery_price

    elif joinery_type == "200X300":
        joinery_price = 250
        if joinery_count > 50:
            joinery_price -= 0.14 * joinery_price
        elif joinery_count > 25:
            joinery_price -= 0.09 * joinery_price
    else:
        error_flag = True

    order_total = joinery_price * joinery_count

    if delivery == "With delivery":
        order_total += 60
    elif delivery == "Without delivery":
        pass
    else:
        error_flag = True

    if joinery_count > 99:
        order_total -= 0.04 * order_total

if error_flag:
    print("Invalid order")
else:
    print(f"{order_total:.2f} BGN")
