activation_key = input()

command = input()

while not command == "Generate":
    split_command = command.split(">>>")
    if split_command[0] == "Contains":
        substring = split_command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif split_command[0] == "Flip":  # Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}
        state_upper_or_lower, start_index, end_index = split_command[1:]  # from index 1 till the end
        start_index, end_index = int(start_index), int(end_index)  # Changes the substring between the given indices
        if state_upper_or_lower == "Upper":
            activation_key = activation_key[0:start_index] + activation_key[start_index:end_index].upper() + \
                             activation_key[end_index:]
        elif state_upper_or_lower == "Lower":
            activation_key = activation_key[0:start_index] + activation_key[start_index:end_index].lower() + \
                             activation_key[end_index:]

        print(activation_key)


    elif split_command[0] == "Slice":  # Deletes the characters between the start and end indices
        # start_index, end_index = int(split_command[1]), int(split_command[2])
        start_index, end_index = split_command[1:]
        start_index, end_index = int(start_index), int(end_index)
        activation_key = activation_key[0:start_index] + activation_key[end_index:]
        print(activation_key)


    command = input()

print(f"Your activation key is: {activation_key}")