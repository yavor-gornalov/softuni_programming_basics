# https://judge.softuni.org/Contests/Compete/Index/2424#4

pens_count = int(input())
markers_count = int(input())
cleaner_liters = int(input())
discount_percent = int(input())

pens_total = pens_count * 5.80
markers_total = markers_count * 7.20
cleaner_total = cleaner_liters * 1.20

total = pens_total + markers_total + cleaner_total
discount = total * discount_percent / 100

final_sum = total - discount

print(final_sum)