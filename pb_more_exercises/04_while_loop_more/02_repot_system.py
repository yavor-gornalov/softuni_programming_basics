# https://judge.softuni.org/Contests/Practice/Index/1684#1

estimated_sum = int(input())

collected_sum = 0
cash_sum = 0
cash_counter = 0
card_sum = 0
card_counter = 0
transaction_counter = 0
while estimated_sum > collected_sum:
    article_price = input()
    if article_price == "End":
        print("Failed to collect required money for charity.")
        break

    transaction_counter += 1
    article_price = int(article_price)
    if transaction_counter % 2 != 0:
        # cash payment
        if article_price > 100:
            print("Error in transaction!")
            continue
        cash_sum += article_price
        cash_counter += 1
        print("Product sold!")
    else:
        # card payment
        if article_price < 10:
            print("Error in transaction!")
            continue
        print("Product sold!")
        card_sum += article_price
        card_counter += 1

    collected_sum += article_price
else:
    cash_average = 0
    card_average = 0
    if cash_counter > 0:
        cash_average = cash_sum / cash_counter
    if card_counter > 0:
        card_average = card_sum / card_counter
    print(f"Average CS: {cash_average:.2f}")
    print(f"Average CC: {card_average:.2f}")
