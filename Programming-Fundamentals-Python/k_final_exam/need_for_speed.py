number_of_cars = int(input())
cars = {}

for i in range(number_of_cars):
    info = input().split('|')
    car = info[0]
    mileage = int(info[1])
    fuel = int(info[2])
    cars[car] = [mileage, fuel]

command = input()
while command != 'Stop':
    command_data = command.split(" : ")
    action = command_data[0]
    car = command_data[1]

    if action == "Drive":
        distance = int(command_data[2])
        fuel = int(command_data[3])

        if fuel > cars[car][1]:  # You need to drive the given distance, and you will need the given fuel
            print("Not enough fuel to make that ride")
        else:   # If the car has the required fuel available in the tank
            cars[car][0] += distance  # increase its mileage with the given distance
            cars[car][1] -= fuel  # decrease its fuel with the given fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if cars[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]


    elif action == 'Refuel':
        fuel = int(command_data[2])
        if cars[car][1] + fuel > 75:   # Each tank can hold a maximum of 75 liters of fuel
            fuel = 75 - cars[car][1]
        cars[car][1] += fuel  # Refill the tank of your car
        print(f"{car} refueled with {fuel} liters")

    elif action == 'Revert':
        kilometers = int(command_data[2])
        if cars[car][0] - kilometers < 10000:  # If the mileage becomes less than 10 000km after it is decreased
            cars[car][0] = 10000   # just set it to 10 000km
        else:
            cars[car][0] -= kilometers  # Decrease the mileage of the given car with the given kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()


for key, value in cars.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")