cake_width = int(input())
cake_height = int(input())

pieces_total = cake_width * cake_height
missing_pieces = 0

while True:
    pieces_per_take = input()
    if pieces_per_take == "STOP":
        break

    pieces_per_take = int(pieces_per_take)
    if pieces_total > pieces_per_take:
        pieces_total -= pieces_per_take
    else:
        missing_pieces = abs(pieces_total - pieces_per_take)
        break

if missing_pieces > 0:
    print(f"No more cake left! You need {missing_pieces} pieces more.")
else:
    print(f"{pieces_total} pieces are left.")
