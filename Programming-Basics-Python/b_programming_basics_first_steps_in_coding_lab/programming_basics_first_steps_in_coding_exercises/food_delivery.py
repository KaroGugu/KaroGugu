chicken_price = 10.35
fish_price = 12.40
vegan_price = 8.15
delivery_price = 2.50

numbers_of_chicken = int(input())
numbers_of_fish = int(input())
numbers_of_vegan = int(input())

sum_of_food = chicken_price * numbers_of_chicken + fish_price * numbers_of_fish + vegan_price * numbers_of_vegan
dessert_price = sum_of_food * 0.20

total_sum = sum_of_food + dessert_price + delivery_price
print(total_sum)
