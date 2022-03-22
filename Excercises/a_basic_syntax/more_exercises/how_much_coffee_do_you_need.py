command = input()

commands_lower = ["coding", "dog", "cat", "movie"]
commands_upper = ['CODING', 'MOVIE', 'DOG', 'CAT']

coffee_counter = 0

while not command == "END":

    if command in commands_lower:
        coffee_counter += 1
    elif command in commands_upper:
        coffee_counter += 2

    command = input()

    if command == "END":
        if coffee_counter > 5:
            print("You need extra sleep")

        else:
            print(coffee_counter)