secret_message = input()

command = input()


while not command == "Reveal":
    split_command = command.split(":|:")
    if split_command[0] == "InsertSpace":
        index = int(split_command[1])   # Inserts a single space at the given index
        secret_message = secret_message[0:index] + " " + secret_message[index:]
        print(secret_message)

    elif split_command[0] == "Reverse":
        substring = split_command[1]
        if substring not in secret_message:
            print("error")
        else:   # If the message contains the given substring, cut it out (= replace it with nothing)
            secret_message = secret_message.replace(substring, "", 1)  # replace only the first occurrence
            reversed_substring = substring[::-1]  # reverse it and add it at the end of the message
            secret_message += reversed_substring
            print(secret_message)

    elif split_command[0] == "ChangeAll":  # Changes all occurrences of the given substring with the replacement text
        substring, replacement_text = split_command[1:]   # substring = split_command[1]   replacement = split_command[2]
        secret_message = secret_message.replace(substring, replacement_text)
        print(secret_message)

    command = input()

print(f"You have a new text message: {secret_message}")