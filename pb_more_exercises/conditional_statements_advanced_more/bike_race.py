juniors = int(input())
seniors = int(input())
route = input()

tax_junior = tax_senior = 0
if route == "trail":
    tax_junior = 5.5
    tax_senior = 7
elif route == "cross-country":
    tax_junior = 8
    tax_senior = 9.5
elif route == "downhill":
    tax_junior = 12.25
    tax_senior = 13.75
elif route == "road":
    tax_junior = 20
    tax_senior = 21.50

tax_total = juniors * tax_junior + seniors * tax_senior

if juniors + seniors >= 50 and route == "cross-country":
    tax_total -= 0.25 * tax_total

tax_total -= 0.05 * tax_total

print(f"{tax_total:.2f}")
