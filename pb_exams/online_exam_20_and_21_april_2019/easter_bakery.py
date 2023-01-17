flour_price = float(input())
flour_kilos = float(input())
sugar_kilos = float(input())
egg_packs = int(input())
leaven_packs = int(input())

sugar_price = (1 - 0.25) * flour_price
egg_pack_price = (1 + 0.10) * flour_price
leaven_pack_price = (1 - 0.80) * sugar_price

flour_cost = flour_kilos * flour_price
sugar_cost = sugar_kilos * sugar_price
eggs_cost = egg_packs * egg_pack_price
leven_cost = leaven_packs * leaven_pack_price

total_cost = flour_cost + sugar_cost + eggs_cost + leven_cost

print(f"{total_cost:.2f}")
