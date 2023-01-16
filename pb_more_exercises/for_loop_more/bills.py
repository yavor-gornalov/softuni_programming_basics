n = int(input())  # months

total_bills = 0
bills = [0, 0, 0, 0]
for _ in range(1, n + 1):
    electricity = float(input())
    bills[0] += electricity
    bills[1] += 20
    bills[2] += 15
    others = electricity + 20 + 15
    bills[3] += (1 + 0.20) * others

print(f"Electricity: {bills[0]:.2f} lv")
print(f"Water: {bills[1]:.2f} lv")
print(f"Internet: {bills[2]:.2f} lv")
print(f"Other: {bills[3]:.2f} lv")
sum_bills = sum(bills)
len_bills = len(bills)
print(f"Average: {(sum(bills) / n):.2f} lv")
