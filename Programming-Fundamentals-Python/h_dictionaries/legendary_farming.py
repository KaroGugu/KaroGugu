data = input()

key_materials = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

items = {"shards": 0, "fragments": 0, "motes": 0}  # the key materials
junk_items = {}

is_obtained = False

while not is_obtained:
    split_data = data.split()

    for index in range(0, len(split_data), 2):
        quantity = int(split_data[index])
        material = split_data[index + 1].lower()  # case-insensitive

        if material in items:
            items[material] += quantity
        else:
            if material not in junk_items:    # we create a junk item list
                junk_items[material] = quantity
            else:                             # we add the item in the junk items list
                junk_items[material] += quantity

        for material, quantity in items.items(): # Keep track of the key materials
            if quantity >= 250:  # the first one that reaches 250, wins the race
                is_obtained = True
                items[material] -= 250
                print(f"{key_materials[material]} obtained!")
                break

        if is_obtained:
            break

    if is_obtained:
        break

    data = input()

# sorted_items = sorted(items.items(), key=lambda kvp: (-kvp[1], kvp[0]))
# sort by quantity in descending order and then by name in ascending order

for material, quantity in items.items():
    print(f"{material}: {quantity}")

# sorted_junks = sorted(junk_items.items(), key=lambda kvp: kvp[0])
# print the collected junk items in the order of appearance
for material, quantity in junk_items.items():
    print(f"{material}: {quantity}")
