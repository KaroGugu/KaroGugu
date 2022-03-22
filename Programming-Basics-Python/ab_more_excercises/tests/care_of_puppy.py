food_kg = int(input())           # Закупеното количество храна за кученцето в килограми

total_eaten_food = 0

command = input()               # команда Adopted или колко грама изяжда кученцето
while command != "Adopted":
    food_eaten = int(command)     # На всеки следващ ред - колко грама изяжда кученцето на всяко хранене
    total_eaten_food += food_eaten

    if command == "Adopted":
        break

    command = input()

food_gr = food_kg * 1000          # количество храна за кученцето в грамове
difference = abs(food_gr - total_eaten_food)    # останала храна / нужно количество храна
if total_eaten_food > food_gr:
    print(f"Food is not enough. You need {difference} grams more.")
else:
    print(f"Food is enough! Leftovers: {difference} grams.")