number_of_cats = int(input())

price_kg_food = 12.45

group_1_counter = 0
group_2_counter = 0
group_3_counter = 0

food_by_cat = 0

for cat in range(1, number_of_cats + 1):
    food_eaten_by_cat = float(input())

    if food_eaten_by_cat >= 100 and food_eaten_by_cat < 200:
        group_1_counter += 1
        food_by_cat += food_eaten_by_cat
    elif food_eaten_by_cat >= 200 and food_eaten_by_cat < 300:
        group_2_counter += 1
        food_by_cat += food_eaten_by_cat
    elif food_eaten_by_cat >= 300 and food_eaten_by_cat < 400:
        group_3_counter += 1
        food_by_cat += food_eaten_by_cat

total_eaten_food = food_by_cat / 1000
total_price_food = total_eaten_food * price_kg_food

print(f"Group 1: {group_1_counter} cats.")
print(f"Group 2: {group_2_counter} cats.")
print(f"Group 3: {group_3_counter} cats.")
print(f"Price for food per day: {round(total_price_food, 2)} lv.")