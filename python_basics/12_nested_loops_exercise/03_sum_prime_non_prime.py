# https://judge.softuni.org/Contests/Compete/Index/2422#2

sum_primes = 0
sum_non_primes = 0
while True:
    number = input()
    if number == "stop":
        break

    number = int(number)
    if number < 0:
        print("Number is negative.")
        continue

    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        sum_primes += number
    else:
        sum_non_primes += number

print(f"Sum of all prime numbers is: {sum_primes}")
print(f"Sum of all non prime numbers is: {sum_non_primes}")
