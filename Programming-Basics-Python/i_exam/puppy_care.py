food_in_kg = float(input())

food_in_gr = food_in_kg * 1000

total_eaten_food = 0

command = input()           # команда Adopted / колко грама изяжда кученцето
while command != "Adopted":
    food_eaten = int(command)

    total_eaten_food += food_eaten

    if command == "Adopted":
        break

    command = input()

diff = abs(food_in_gr - total_eaten_food)
if total_eaten_food <= food_in_gr:
    print(f"Food is enough! Leftovers: {int(diff)} grams.")
else:
    print(f"Food is not enough. You need {int(diff)} grams more.")