first_symbol = input()
second_symbol = input()

list = []

def character_in_range():
    for char in range(ord(first_symbol), ord(second_symbol) + 1):
        current_character = chr(char)
        list.append(current_character)

    list.remove(first_symbol)
    list.remove(second_symbol)
    print(" ".join(list))

character_in_range()