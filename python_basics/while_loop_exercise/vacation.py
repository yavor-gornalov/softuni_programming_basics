estimated_money = float(input())
balance = float(input())

spend_counter = 0
days_counter = 0

while spend_counter < 5 and balance < estimated_money:
    transaction_type = input()
    transaction_value = float(input())
    days_counter += 1

    if transaction_type == "spend":
        spend_counter += 1
        if balance > transaction_value:
            balance -= transaction_value
        else:
            balance = 0
    elif transaction_type == "save":
        spend_counter = 0
        balance += transaction_value

if spend_counter < 5:
    print(f"You saved the money for {days_counter} days.")
else:
    print("You can't save the money.")
    print(f"{days_counter}")
