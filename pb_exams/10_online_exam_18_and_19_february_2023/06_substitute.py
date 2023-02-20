# https://judge.softuni.org/Contests/Compete/Index/3880#5

k_range = int(input())  # [0:8]
l_range = int(input())  # [0:9]
m_range = int(input())  # [0:8]
n_range = int(input())  # [0:9]

counter = 0
for k_digit in range(k_range, 9):
    if k_digit % 2:
        continue
    for l_digit in range(9, l_range - 1, -1):
        if not l_digit % 2:
            continue
        for m_digit in range(m_range, 9):
            if m_digit % 2:
                continue
            for n_digit in range(9, n_range - 1, -1):
                if not n_digit % 2:
                    continue
                if not counter < 6:
                    break
                left_sub = f"{k_digit}{l_digit}"
                right_sub = f"{m_digit}{n_digit}"
                if not left_sub == right_sub:
                    print(f"{left_sub} - {right_sub}")
                    counter += 1
                else:
                    print("Cannot change the same player.")
