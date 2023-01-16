from math import ceil

people_count = int(input())
entry_tax_per_person = float(input())
lounger_price = float(input())
umbrella_price = float(input())

entry_tax = people_count * entry_tax_per_person
lounger_tax = ceil(0.75 * people_count) * lounger_price
umbrella_tax = ceil(people_count / 2) * umbrella_price

total_tax = entry_tax + lounger_tax + umbrella_tax

print(f"{total_tax:.2f} lv.")
