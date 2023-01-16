total = 0
while True:
    deposit = input()
    if deposit == "NoMoreMoney":
        break
    deposit = float(deposit)
    if deposit < 0:
        print("Invalid operation!")
        break
    total += deposit
    print(f"Increase: {deposit:.2f}")

print(f"Total: {total:.2f}")
