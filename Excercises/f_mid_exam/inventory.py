collected_items = input().split(", ")

command = input()
while not command == "Craft!":

    data = command.split(" - ")
    action = data[0]
    item = data[1]

    if action == "Collect":
        if item not in collected_items:
            collected_items.append(item)

    elif action == "Drop":
        if item in collected_items:
            collected_items.remove(item)

    elif action == "Combine Items":
        old_item, new_item = data[1].split(":")
        if old_item in collected_items:
            old_item_index = collected_items.index(old_item)
            collected_items.insert(old_item_index + 1, new_item)

    elif action == "Renew":
        if item in collected_items:
            collected_items.remove(item)
            collected_items.append(item)

    command = input()

print(", ".join(collected_items))
