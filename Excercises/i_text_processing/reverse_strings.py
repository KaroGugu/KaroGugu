command = input()

while not command == "end":
    reversed_word = command[::-1]
    print(f"{command} = {reversed_word}")

    command = input()