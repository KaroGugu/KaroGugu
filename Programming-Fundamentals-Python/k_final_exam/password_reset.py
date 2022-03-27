text = input()

command = input()


while not command == "Done":
    split_command = command.split()
    action = split_command[0]

    if action == "TakeOdd":
        text = ''.join([x for i, x in enumerate(text) if i % 2 != 0])
        print(text)

    elif action == "Cut":
        index = int(split_command[1])
        length = int(split_command[2])

        text = text[:index] + text[index+length:]  # with the given length starting from the given index
        print(text)


    elif action == "Substitute":
        substring = split_command[1]
        substitute = split_command[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {text}")