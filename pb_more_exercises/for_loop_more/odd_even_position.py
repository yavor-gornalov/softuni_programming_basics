from sys import maxsize

n = int(input())

odd_sum = even_sum = 0
odd_min = even_min = maxsize
odd_max = even_max = -maxsize

for i in range(1, n + 1):
    number = float(input())
    if i % 2 != 0:
        odd_sum += number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number
    else:
        even_sum += number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number

odd_extremum = odd_min > maxsize or odd_max > -maxsize
even_extremum = even_min > maxsize or even_max > -maxsize

print(f"OddSum={odd_sum:.2f},")
if odd_extremum:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
else:
    print(f"OddMin=No,")
    print(f"OddMax=No,")

print(f"EvenSum={even_sum:.2f},")
if even_extremum:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
else:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
