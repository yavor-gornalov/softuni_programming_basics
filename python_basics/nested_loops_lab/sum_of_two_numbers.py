start_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())
is_found = False

combinations_counter = 0
for a in range(start_of_interval, end_of_interval + 1):
    for b in range(start_of_interval, end_of_interval + 1):
        combinations_counter += 1
        if a + b == magic_number:
            is_found = True
            print(f"Combination N:{combinations_counter} ({a} + {b} = {magic_number})")
            break
    if is_found:
        break

if not is_found:
    print(f"{combinations_counter} combinations - neither equals {magic_number}")
