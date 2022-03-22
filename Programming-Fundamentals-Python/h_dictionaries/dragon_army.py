number_of_dragons = int(input())

dragons_dict = {}
dragons_types_list = []   # black, red, gold, azure
default_stats = (45, 250, 10)  # damage, health, and armor  # If a stat is missing will be marked by "null"


for dragon in range(number_of_dragons):
    dragon_type, name, damage, health, armor = input().split()  # The input

    damage, health, armor = (default_stats[i] if x == "null" else int(x) for i, x in enumerate((damage, health, armor)))

    key = (dragon_type, name)
    value = (damage, health, armor)
    dragons_dict[key] = value

    if dragon_type not in dragons_types_list:
        dragons_types_list.append(dragon_type)

for dragon_type in dragons_types_list:
    stats = [value for key, value in dragons_dict.items() if key[0] == dragon_type]
    damage, health, armor = [sum(item) / len(item) for item in zip(*stats)]
    print(f"{dragon_type}::({damage:.2f}/{health:.2f}/{armor:.2f})")

    filtered_dragons = {key[1]: value for key, value in dragons_dict.items() if key[0] == dragon_type}
    output = {key: value for key, value in sorted(filtered_dragons.items(), key=lambda item: item[0])}

    for key, value in output.items():
        print(f'-{key} -> damage: {value[0]}, health: {value[1]}, armor: {value[2]}')