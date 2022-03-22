
command = input()

cities = {}


while not command == "Sail":
    city, population, gold = command.split("||")
    population = int(population)
    gold = int(gold)

    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:  # a city that has already been received
        cities[city]["population"] += population  # to increase the population and gold with the given values
        cities[city]["gold"] += gold

    command = input()

data = input()
while not data == "End":
    split_data = data.split("=>")
    if split_data[0] == "Plunder":
        city = split_data[1]
        people = int(split_data[2])
        gold = int(split_data[3])

        cities[city]["population"] -= people  # killing the given number of people
        cities[city]["gold"] -= gold  # stealing the respective amount of gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0: # If any of those two values is zero
            del cities[city]  # the town is disbanded => remove it from your collection of targeted cities
            print(f"{city} has been wiped off the map!")


    elif split_data[0] == "Prosper":
        city = split_data[1]
        gold = int(split_data[2])

        if gold < 0:
            print("Gold added cannot be a negative number!")
            data = input()
            continue
        cities[city]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")

    data = input()

if not cities:  # If there are no settlements left to plunder
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

else:
    # print all of them, sorted by their gold in descending order, then by their name in ascending order
    # sorted_result = sorted(cities.items(), key= lambda tkvp: (-tkvp[1]['gold'], tkvp[0]))
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, data in cities.items():
        print(f"{city} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")
