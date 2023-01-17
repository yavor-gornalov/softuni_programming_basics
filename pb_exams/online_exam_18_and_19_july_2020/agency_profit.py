company = input()
adult_tickets_count = int(input())
child_tickets_count = int(input())
adult_tickets_price = float(input())
service_price = float(input())

child_tickets_price = (1 - 0.70) * adult_tickets_price

adult_tickets_profit = adult_tickets_count * (adult_tickets_price + service_price)
child_tickets_profit = child_tickets_count * (child_tickets_price + service_price)

profit_total = adult_tickets_profit + child_tickets_profit
profit_neto = 0.20 * profit_total

print(f"The profit of your agency from {company} tickets is {profit_neto:.2f} lv.")
