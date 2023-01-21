# https://judge.softuni.org/Contests/Practice/Index/1054#3

period = int(input())

medics = 7
treated_patients = 0
untreated_patients = 0
for day in range(1, period + 1):
    if day % 3 == 0:
        if treated_patients < untreated_patients:
            medics += 1
    patients = int(input())
    if medics < patients:
        untreated_patients += patients - medics
        treated_patients += medics
    else:
        treated_patients += patients

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
