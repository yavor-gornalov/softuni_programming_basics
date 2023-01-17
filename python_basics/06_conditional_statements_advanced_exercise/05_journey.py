# https://judge.softuni.org/Contests/Compete/Index/2416#4

budget = float(input())
season = input()

destination = ''
rest_type = ''
percent = 0

if budget <= 100:
    destination = 'Bulgaria'
    # season == summer
    rest_type = 'Camp'
    percent = 30
    if season == 'winter':
        rest_type = 'Hotel'
        percent = 70

elif budget <= 1000:
    destination = 'Balkans'
    # season == summer
    rest_type = 'Camp'
    percent = 40
    if season == 'winter':
        rest_type = 'Hotel'
        percent = 80

else:
    destination = 'Europe'
    # season == summer
    rest_type = 'Hotel'
    percent = 90

cost = budget * percent / 100

print(f"Somewhere in {destination}")
print(f"{rest_type} - {cost:.2f}")
