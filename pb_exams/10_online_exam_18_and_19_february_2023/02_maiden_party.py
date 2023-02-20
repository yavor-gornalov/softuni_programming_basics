# https://judge.softuni.org/Contests/Compete/Index/3880#1

LOVE_MESSAGE = 0.60
WAX_ROSE = 7.20
KEY_CHAIN = 3.60
CARTOON = 18.20
LUCKY_SURPRISE = 22.00

maiden_party_price = float(input())
love_messages_count = int(input())
wax_roses_count = int(input())
key_chains_count = int(input())
cartoons_count = int(input())
lucky_surprises_count = int(input())

total_articles_count = love_messages_count + wax_roses_count + \
                       key_chains_count + cartoons_count + lucky_surprises_count

total_articles_price = love_messages_count * LOVE_MESSAGE + wax_roses_count * WAX_ROSE + \
                       key_chains_count * KEY_CHAIN + cartoons_count * CARTOON + lucky_surprises_count * LUCKY_SURPRISE

total_articles_price = (1 - 0.35) * total_articles_price if total_articles_count >= 25 else total_articles_price

profit = (1 - 0.10) * total_articles_price

if profit >= maiden_party_price:
    print(f"Yes! {profit - maiden_party_price:.2f} lv left.")
else:
    print(f"Not enough money! {maiden_party_price - profit:.2f} lv needed.")
