def is_index_valid(index, string):
    if 0 <= index < len(string):
        return True
    return False


stops = input()

command = input()
while not command == "Travel":
    split_command, val_1, val_2 = command.split(":")

    if split_command == "Add Stop":   # if split_command.startswith("Add")
        index = int(val_1)
        if is_index_valid(index, stops):  # if the index is valid
            stops = stops[:index] + val_2 + stops[index:]       # Insert the given string at that index

        print(stops)

    elif split_command == "Remove Stop":  # Remove the elements of the string from the start to the end index
        start_index = int(val_1)
        end_index = int(val_2)
        if is_index_valid(start_index, stops) and is_index_valid(end_index, stops):
            stops = stops[:start_index] + stops[end_index+1:]  # the end index (inclusive)
        print(stops)

    elif split_command == "Switch":
        if val_1 in stops:
            stops = stops.replace(val_1, val_2)
        print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")