text = input()


command = input()

while not command == "Finish":
    split_command = command.split()

    if split_command[0] == "Replace":
        current_char, new_char = split_command[1:]
        text = text.replace(current_char, new_char)
        print(text)

    elif split_command[0] == "Cut":
        start_index, end_index = split_command[1:]
        start_index = int(start_index)
        end_index = int(end_index)

        if 0 <= start_index <= len(text) and 0 <= end_index <= len(text):
            text = text[:start_index] + text[end_index + 1:]
            print(text)
        else:
            print("Invalid indices!")


    elif split_command[0] == "Make":
        action = split_command[1]

        if action == "Upper":
            text = text.upper()
        elif action == "Lower":
            text = text.lower()
        print(text)

    elif split_command[0] == "Check":
        string = split_command[1]

        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")

    elif split_command[0] == "Sum":
        start_index, end_index = split_command[1:]
        start_index = int(start_index)
        end_index = int(end_index)

        substring = text[start_index:end_index + 1]
        if 0 <= start_index <= len(text) and 0 <= end_index <= len(text):
            sum_of_char_of_substring = sum([ord(el) for el in substring])
            print(sum_of_char_of_substring)
        else:
            print("Invalid indices!")

    command = input()