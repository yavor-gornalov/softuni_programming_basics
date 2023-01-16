budget = float(input())
season = input()

if season == "Summer":
    destination = "Alaska"
elif season == "Winter":
    destination = "Morocco"

accommodation = ''
percent = 0
if budget <= 1000:
    accommodation = "Camp"
    percent = 0.65
    destination = "Alaska"
    if season == "Winter":
        destination = "Morocco"
        percent = 0.45
elif budget <= 3000:
    accommodation = "Hut"
    percent = 0.80
    destination = "Alaska"
    if season == "Winter":
        destination = "Morocco"
        percent = 0.60
else:
    accommodation = "Hotel"
    percent = 0.90
    destination = "Alaska"
    if season == "Winter":
        destination = "Morocco"

cost = percent * budget

print(f"{destination} - {accommodation} - {cost:.2f}")
