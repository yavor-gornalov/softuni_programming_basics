# https://judge.softuni.org/Contests/Compete/Index/2424#7

annual_tax = int(input())
trainers_price = annual_tax * (1 - 0.40)
equip_price = trainers_price * (1 - 0.20)
ball_price = equip_price / 4
acc_price = ball_price / 5

total_price = annual_tax + trainers_price + equip_price + ball_price + acc_price

print(total_price)
