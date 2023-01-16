# https://judge.softuni.org/Contests/Compete/Index/2424#2

deposit_sum = float(input())
deposit_term = int(input())
interest_percent = float(input())

interest_per_year = deposit_sum * interest_percent / 100
interest_per_month = interest_per_year / 12

total_interest = deposit_sum + deposit_term * interest_per_month

print(total_interest)
