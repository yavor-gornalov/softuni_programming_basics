start_num = int(input())
end_num = int(input())
magic_num = int(input())

iteration = 0
flag = False
while True:
    for i in range(start_num, end_num + 1):
        for j in range(start_num, end_num + 1):
            iteration += 1
            if i + j == magic_num:
                print(f"Combination N:{iteration} ({i} + {j} = {magic_num})")
                flag = True
                break
            elif i == end_num and j == end_num:
                print(f"{iteration} combinations - neither equals {magic_num}")
                flag = True
                break
        if flag:
            break
    if flag:
        break

