password = 'con'
current_pass = ''
sentence = ''

while True:
    letter = input()
    if letter == "End":
        if sentence != '':
            i = len(sentence) - 1
            while i >= 0:
                ch = sentence[i]
                if ch != ' ':
                    sentence = sentence[:i]
                    i -= 1
                else:
                    break
        break

    if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
        if letter in password:
            if letter not in current_pass:
                current_pass += letter
                if len(current_pass) < 3:
                    continue
                else:
                    current_pass = ''
                    sentence += ' '
                    continue

        sentence += letter

print(sentence)
