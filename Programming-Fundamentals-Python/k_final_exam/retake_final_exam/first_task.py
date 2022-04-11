username = input()

command = input()

while not command == "Registration":
    split_command = command.split()

    if split_command[0] == "Letters":
        lower_or_upper = split_command[1]
        if lower_or_upper == "Lower":
            username = username.lower()
        elif lower_or_upper == "Upper":
            username = username.upper()
        print(username)

    elif split_command[0] == "Reverse":
        start_index, end_index = split_command[1:]
        start_index = int(start_index)
        end_index = int(end_index)

        if 0 < start_index <= len(username) and 0 < end_index <= len(username):
            substring = username[start_index:end_index + 1]
            reversed_substring = substring[::-1]
            print(reversed_substring)

    elif split_command[0] == "Substring":
        substring = split_command[1]
        if substring not in username:
            print(f"The username {username} doesn't contain {substring}.")
        else:
            username = username.replace(substring, "")
            print(username)


    elif split_command[0] == "Replace":
        char = split_command[1]
        username = username.replace(char, "-")
        print(username)

    elif split_command[0] == "IsValid":
        char = split_command[1]
        if char in username:
            print("Valid")
        else:
            print(f"{char} must be contained in your username.")

    command = input()