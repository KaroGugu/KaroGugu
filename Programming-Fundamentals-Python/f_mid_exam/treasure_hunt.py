treasure_chest = input().split('|')

sum_items = 0

while True:
    command = input().split()
    if command[0] == 'Yohoho!':
        break

    elif command[0] == 'Loot':
        for i in range(len(command)):
            if i == 0:
                continue
            item = command[i]
            if item not in treasure_chest:
                treasure_chest.insert(0, item)   # Insert the items at the beginning of the chest

    elif command[0] == 'Drop':
        index = int(command[1])
        if 0 <= index < len(treasure_chest):
            x = treasure_chest.pop(index)    # Remove the loot at the given position
            treasure_chest.append(x)       # add it at the end of the treasure chest
        else:                         # If the index is invalid, skip the command
            continue

    elif command[0] == 'Steal':
        count = int(command[1])
        if count >= len(treasure_chest):    # If the chest is empty
            removed = treasure_chest
            print(', '.join(removed))
            print('Failed treasure hunt.')
            exit()
        else:   # If there are fewer items than the given count, remove as much as there are.
            removed = treasure_chest[-count:]
            del treasure_chest[-count:]    # Someone steals the last count loot items
            print(', '.join(removed))

if len(treasure_chest) > 0:
    for i in range(len(treasure_chest)):
        sum_items += len(treasure_chest[i])

    average = f'{sum_items / len(treasure_chest):.2f}'
# average treasure gain,which is the sum of all treasure items length divided by the count of all items inside the chest
    print(f'Average treasure gain: {average} pirate credits.')