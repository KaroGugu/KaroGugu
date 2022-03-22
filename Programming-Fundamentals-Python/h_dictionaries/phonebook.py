def phone_book_information(number_of_lines, phone_book):
    for x in range(number_of_lines):  # receive a number – N.
        name = input()    # perform a search of contact by name
        if name not in phone_book:  # In case the contact isn't found
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {phone_book[name]}")

    return True



def phonebook():

    phone_book = {}
    condition = False

    while True:
        contact_info = input().split("-")  # Each entry should have a name and a number (both strings) separated

        if contact_info[0].isdigit():
            condition = phone_book_information(int(contact_info[0]), phone_book)

        else:
            phone_book[contact_info[0]] = contact_info[1]


        if condition:
            break


phonebook()