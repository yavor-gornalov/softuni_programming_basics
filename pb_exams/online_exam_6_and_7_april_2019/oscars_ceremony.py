hall_rent = int(input())

statuettes = (1 - 0.30) * hall_rent
catering = (1 - 0.15) * statuettes
sounding = catering / 2

total = hall_rent + statuettes + catering + sounding

print(f"{total:.2f}")
