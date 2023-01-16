resto = float(input())
resto_in_cents = int(resto * 100)

cents = [200, 100, 50, 20, 10, 5, 2, 1]

coins_count = index = 0
while resto_in_cents > 0:
    if resto_in_cents >= cents[index]:
        resto_in_cents -= cents[index]
        coins_count += 1
    else:
        index += 1

print(coins_count)
