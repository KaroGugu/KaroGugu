number_of_heroes = int(input())
heroes = {}

for i in range(number_of_heroes):
    hero_name, hp, mp = input().split()
    heroes[hero_name] = {"HP": int(hp), "MP": int(mp)}

data = input()

while not data == "End":
    split_data = data.split(" - ")

    if split_data[0] == "CastSpell":
        hero_name, mp_needed, spell_name = split_data[1:]
        mp_needed = int(mp_needed)
        if heroes[hero_name]["MP"] >= mp_needed:  # # If the hero has the required MP, reducing his MP
            heroes[hero_name]["MP"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
        else:  # If the hero is unable to cast the spell print
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")


    elif split_data[0] == "TakeDamage":
        hero_name, damage, attacker = split_data[1:]
        damage = int(damage)
        if heroes[hero_name]["HP"] - damage <= 0:  # Reduce the hero HP by the given damage amount
            del heroes[hero_name]  # If the hero has died, remove him from your party
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            heroes[hero_name]["HP"] -= damage  # Reduce the hero HP by the given damage amount
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")


    elif split_data[0] == "Recharge":
        hero_name, amount = split_data[1:]
        amount = int(amount)
        if heroes[hero_name]["MP"] + amount > 200:  # hero increases his MP
            print(f"{hero_name} recharged for {200 - heroes[hero_name]['MP']} MP!")
            heroes[hero_name]["MP"] = 200  # MP can't go over the maximum value
        else:
            heroes[hero_name]["MP"] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif split_data[0] == "Heal":
        hero_name, amount = split_data[1:]
        amount = int(amount)
        if heroes[hero_name]["HP"] + amount > 100:  # the HP can't go over the maximum value
            print(f"{hero_name} healed for {100 - heroes[hero_name]['HP']} HP!")
            heroes[hero_name]["HP"] = 100
        else:
            heroes[hero_name]["HP"] += amount
            print(f"{hero_name} healed for {amount} HP!")
    data = input()


# Print alive members sorted by their HP in descending order, then by their name in ascending order
# sorted_heroes = sorted(heroes.items(), key=lambda kvpt: (-kvpt[1]['HP'], kvpt[0]))
for name, values in heroes.items():
    print(name)
    print(f"  HP: {values['HP']}")
    print(f"  MP: {values['MP']}")