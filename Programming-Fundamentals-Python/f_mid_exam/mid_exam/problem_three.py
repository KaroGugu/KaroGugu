shelf_with_books = input().split("&")

command = input()
while command != "Done":
    current_command = command.split(" | ")
    action = current_command[0]
    book_name = current_command[1]

    if action == "Add Book":
        if book_name not in shelf_with_books:
            shelf_with_books.insert(0, book_name)

    elif action == "Take Book":
        if book_name in shelf_with_books:
            shelf_with_books.remove(book_name)

    elif action == "Swap Books":
        second_book = current_command[2]
        if book_name in shelf_with_books and second_book in shelf_with_books:
            first_index = shelf_with_books.index(book_name)
            second_index = shelf_with_books.index(second_book)
            shelf_with_books[first_index], shelf_with_books[second_index] = \
                shelf_with_books[second_index], shelf_with_books[first_index]

    elif action == "Insert Book":
        if book_name not in shelf_with_books:
            shelf_with_books.append(book_name)

    elif action == "Check Book":
        index = int(book_name)
        if 0 <= index < len(shelf_with_books):
            result = shelf_with_books[index]
            print(result)

    command = input()

print(", ".join(shelf_with_books))