products = input().split("!")

command = input()
while command != "Go Shopping!":
    current_command = command.split()
    action = current_command[0]
    item = current_command[1]

    if action == "Urgent":
        if item not in products:  # If the item already exists, skip this command.
            products.insert(0, item)  # add the item at the start of the list.

    if action == "Unnecessary":
        if item in products:  # only if it exists in the list
            products.remove(item)  # remove the item with the given name

    if action == "Correct":
        if item in products:  # if the item with the given old name exists
            new_item = current_command[2]
            index_old_item = products.index(item)
            products.remove(item)
            products.insert(index_old_item, new_item)  # change old item's name with the new one

    if action == "Rearrange":
        if item in products:  # if the grocery exists in the list
            products.remove(item)  # remove it from its current position
            products.append(item)  # add it at the end of the list

    command = input()

print(", ".join(products))
