from math import floor, ceil

days_travel = int(input())
food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())     # from gram into kg       1 kg = 1000 g

dog = days_travel * dog_food_per_day
cat = days_travel * cat_food_per_day
turtle = (days_travel * turtle_food_per_day) / 1000

total_food_eaten = dog + cat + turtle
difference = abs(food - total_food_eaten)

if food >= total_food_eaten:
    print(f'{floor(difference)} kilos of food left.')
else:
    print(f'{ceil(difference)} more kilos of food are needed.')