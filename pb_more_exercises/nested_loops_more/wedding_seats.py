sector = input()
first_sector_rows = int(input())
places_count = int(input())

sector_rows = first_sector_rows
places_total = 0
for sec in range(ord("A"), ord(sector) + 1):
    for row in range(1, sector_rows + 1):
        places = places_count
        if row % 2 == 0:
            places = places_count + 2
        for pl in range(ord("a"), ord("a") + places):
            places_total += 1
            print(f"{chr(sec)}{row}{chr(pl)}")
    sector_rows += 1
print(places_total)
