# https://judge.softuni.org/Contests/Practice/Index/1745#9

powerful_word = ""
word_power = 0
while True:
    current_word_power = 0
    word = input()
    if word == "End of words":
        break

    for ch in word:
        current_word_power += ord(ch)

    if word[0].lower() in "aeiouy":
        current_word_power = round(current_word_power * len(word))
    else:
        current_word_power = round(current_word_power / len(word))

    if current_word_power > word_power:
        word_power = current_word_power
        powerful_word = word

print(f"The most powerful word is {powerful_word} - {word_power}")
