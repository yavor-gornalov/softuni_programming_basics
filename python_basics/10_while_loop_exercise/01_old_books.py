# https://judge.softuni.org/Contests/Compete/Index/2420#0

search_book = input()

books_checked = 0
not_found = False
while True:
    current_book = input()
    if search_book == current_book:
        break
    elif current_book == "No More Books":
        not_found = True
        break
    books_checked += 1

if not_found:
    print("The book you search is not here!")
    print(f"You checked {books_checked} books.")
else:
    print(f"You checked {books_checked} books and found it.")
