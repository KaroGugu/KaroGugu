import math

days = int(input())
total_food = float(input())

eaten_food = 0
dog = 0
cat = 0
biscuits = 0

for day in range(1, days + 1):
    food_eaten_by_dog = int(input())
    dog += food_eaten_by_dog
    food_eaten_by_cat = int(input())
    cat += food_eaten_by_cat
    eaten_food += food_eaten_by_cat + food_eaten_by_dog

    if day % 3 == 0:              # На всеки трети ден получават награда - бисквитки
        biscuits += (food_eaten_by_cat + food_eaten_by_dog) * 0.10  # 10% от общо изядената храна за деня.

print(f'Total eaten biscuits: {round(biscuits)}gr.')   # закръглено до най – близкото цяло число
print(f'{eaten_food / total_food * 100:.2f}% of the food has been eaten.') # колко процента от първоначалното количество
                                                                            # обща храна са изяли
print(f'{dog / eaten_food * 100:.2f}% eaten from the dog.') # колко процента от изядената храна е изяло кучето
print(f'{cat / eaten_food * 100:.2f}% eaten from the cat.') # колко процента от изядената храна е изяла котката