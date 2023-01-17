# https://judge.softuni.org/Contests/Practice/Index/1642#3

price_vegetables = float(input())
price_fruits = float(input())
weight_vegetables = int(input())
weight_fruits = int(input())
euro = 1.94
total_vegetables = price_vegetables * weight_vegetables
total_fruits = price_fruits * weight_fruits
total_euro = (total_fruits + total_vegetables) / euro

print('%.2f' % total_euro)
