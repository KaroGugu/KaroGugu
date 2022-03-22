numbers = input().split()
command = input()

while command != "Finish":
    current_command = command.split()
    action = current_command[0]
    value = current_command[1]

    if action == "Add":
        numbers.append(value)

    elif action == "Remove":
        if value in numbers:
            numbers.remove(value)
        else:
            continue

    elif action == "Replace":
        replacement = current_command[2]
        if value in numbers:
            index_value = numbers.index(value)
            numbers.insert(index_value, replacement)
            numbers.remove(value)
        else:
            continue

    elif action == "Collapse":
        for num in numbers:
            if num <= value:
                numbers.remove(num)
            else:
                continue

    command = input()

print(*numbers)