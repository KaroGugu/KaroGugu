numbers = int(input())

plants = {}

for line in range(numbers):
    plant_name, rarity = input().split("<->")
    rarity = int(rarity)
    plants[plant_name] = {"rarity": rarity, "ratings": []}  # (store all ratings)


command = input()
while not command == "Exhibition":
    split_command, command_params = command.split(": ")  # Rate: {plant} - {rating}"

    if split_command == "Rate":
        plant, rating = command_params.split(" - ")
        rating = int(rating)
        if plant in plants:
            plants[plant]['ratings'].append(rating)   # add the given rating to the plant
        else:
            print('error')

    elif split_command == "Update":
        plant, new_rarity = command_params.split(" - ")
        new_rarity = int(new_rarity)
        if plant in plants:
            plants[plant]['rarity'] = new_rarity  # update the rarity of the plant with the new one
        else:
            print('error')

    elif split_command == "Resent":
        plant = command_params
        if plant in plants:
            plants[plant]['rating'].clear()  # plants[plant]['rating'] = []   # remove all the ratings of the given plant
        else:
            print("error")

    command = input()

# plants should be sorted average rating
for plant_name, value in plants.items():
    if value['ratings']:
        average = sum(value['ratings']) / len(value['ratings'])
    else:
        average = 0
    plants[plant_name]['average'] = average

# plants should be sorted by rarity descending, then by average rating descening
# sorted_plants = sorted(plants.items(), key=lambda tkvp: (-tkvp[1]['rarity'],-tkvp[1]['average']))
# sorted_plants = sorted(plants.items(), key=lambda tkvp: (tkvp[1]['rarity'],tkvp[1]['average'], reverse=True))

print("Plants for the exhibition:")
for plant, values in plants.items():
    print(f"- {plant}; Rarity: {values['rarity']}; Rating: {values['average']:.2f}")