number_of_cars = int(input())

cars = {}

for i in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}

command = input()

while not command == "Stop":
    split_command = command.split(" : ")
    command_name = split_command[0]

    if command_name == "Drive":
        car, distance, fuel = split_command[1:]
        distance = int(distance)
        fuel = int(fuel)

        if cars[car]["fuel"] < fuel:  # You need to drive the given distance, and you will need the given fuel
            print("Not enough fuel to make that ride")

        else:   # If the car has the required fuel available in the tank,
            cars[car]["mileage"] += distance  # increase its mileage with the given distance
            cars[car]["fuel"] -= fuel  # decrease its fuel with the given fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if cars[car]["mileage"] > 100000:
            print(f"Time to sell the {car}!")
            cars.pop(car)


    elif command_name == "Refuel":
        car, fuel = split_command[1:]
        fuel = int(fuel)

        cars[car]["fuel"] += fuel  # Refill the tank of your car
        if cars[car]["fuel"] > 75:   # Each tank can hold a maximum of 75 liters of fuel
            cars[car]["fuel"] = 75
            print(f"{car} refueled with {75 - cars[car]['fuel']} liters")
        else:
            print(f"{car} refueled with {fuel} liters")


    elif command_name == "Revert":
        car, kilometers = split_command[1:]
        kilometers = int(kilometers)

        cars[car]["mileage"] -= kilometers  # Decrease the mileage of the given car with the given kilometers
        if cars[car]["mileage"] < 10000:  # If the mileage becomes less than 10 000km after it is decreased
            cars[car]["mileage"] = 10000       # just set it to 10 000km
            break

        print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for car in cars:
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")