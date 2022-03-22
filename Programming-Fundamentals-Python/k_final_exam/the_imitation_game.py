encrypted_message = input()

command = input()

while not command == "Decode":
    split_command = command.split("|")

    if split_command[0] == "Move":  # Moves the first n letters to the back of the string
        number_of_letters = int(split_command[1])
        letters_to_move = encrypted_message[:number_of_letters]
        first_part = encrypted_message[number_of_letters:]
        encrypted_message = first_part + letters_to_move

    elif split_command[0] == "Insert":  # Inserts the given value before the given index
        index = int(split_command[1])
        value = split_command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif split_command[0] == "ChangeAll":
        substring = split_command[1]
        replacement = split_command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {encrypted_message}")