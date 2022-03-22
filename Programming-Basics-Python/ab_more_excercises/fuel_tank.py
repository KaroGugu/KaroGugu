fuel = input()
liters = int(input())

if liters >= 25:
    if fuel == "Diesel":
        print("You have enough diesel.")
    elif fuel == "Gasoline":
        print("You have enough gasoline.")
    elif fuel == "Gas":
        print("You have enough gas.")
    else:
        print("Invalid fuel!")
else:
    if fuel == "Diesel":
        print("Fill your tank with diesel!")
    elif fuel == "Gasoline":
        print("Fill your tank with gasoline!")
    elif fuel == "Gas":
        print("Fill your tank with gas!")
    else:
        print("Invalid fuel!")