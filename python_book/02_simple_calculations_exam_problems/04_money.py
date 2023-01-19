# https://judge.softuni.org/Contests/Practice/Index/1048#3

bitcoin_amount = int(input())
yuan_amount = float(input())
commission = float(input())

bgn_amount = bitcoin_amount * 1168
usd_amount = yuan_amount * 0.15
bgn_amount += usd_amount * 1.76

euro_amount = bgn_amount / 1.95
euro_amount -= (commission / 100) * euro_amount

print(f"{euro_amount:.2f}")
