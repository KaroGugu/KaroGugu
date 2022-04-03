command = input()

heroes = {}

while not command == "End":
    split_command = command.split()

    if split_command[0] == "Enroll":
        hero_name = split_command[1]
        if hero_name not in heroes:
            heroes[hero_name] = hero_name
        else:
            print(f"{hero_name} is already enrolled.")

    elif split_command[0] == "Learn":
        hero_name, spell_name = split_command[1:]

        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name in heroes:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            heroes[hero_name] = spell_name

    elif split_command[0] == "Unlearn":
        hero_name, spell_name = split_command[1:]

        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes:
                print(f"{hero_name} doesn't know {spell_name}.")
        else:
            del heroes[spell_name]


    command = input()

print("Heroes:")

for hero, spell in heroes.items():
    print(f"== {hero}: {spell}")