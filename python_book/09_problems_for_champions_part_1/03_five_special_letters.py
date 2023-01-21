# https://judge.softuni.org/Contests/Practice/Index/1061#2

start_weight = int(input())
end_weight = int(input())


def remove_duplicate(word):
    new_word = ""
    for letter in word:
        if letter not in new_word:
            new_word += letter
    return new_word


def weight(word):
    total = 0
    for index, letter in enumerate(word):
        if letter == 'a':
            total += (index + 1) * 5
        elif letter == 'b':
            total += (index + 1) * -12
        elif letter == 'c':
            total += (index + 1) * 47
        elif letter == 'd':
            total += (index + 1) * 7
        elif letter == 'e':
            total += (index + 1) * -32
    return total


pattern = 'abcde'
possible_combination = ''
found = False
for ch1 in pattern:
    for ch2 in pattern:
        for ch3 in pattern:
            for ch4 in pattern:
                for ch5 in pattern:
                    possible_combination = ch1 + ch2 + ch3 + ch4 + ch5
                    without_duplicates = remove_duplicate(possible_combination)
                    weight_total = weight(without_duplicates)

                    if start_weight <= weight_total <= end_weight:
                        found = True
                        print(possible_combination, end=" ")

if not found:
    print("No")
