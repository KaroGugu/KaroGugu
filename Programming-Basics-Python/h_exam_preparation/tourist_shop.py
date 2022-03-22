budget = float(input())

cost = 0
products_counter = 0
needed_money = 0

budget_is_enough = True

while True:
    name_of_product = input()            # до получаване на команда "Stop"
    if name_of_product == "Stop":
        break

    price_of_product = float(input())
    products_counter += 1

    if products_counter % 3 == 0:        # Всеки трети продукт е на половин цена.
        price_of_product /= 2

    if price_of_product > budget:        # продукт, чиято цена е по-висока от останалите пари
        needed_money = price_of_product - budget
        budget_is_enough = False
        break

    cost += price_of_product
    budget -= price_of_product

if budget_is_enough:   # budget_is_enough = True
    print(f"You bought {products_counter} products for {cost:.2f} leva.")
else:
    diff = abs(budget - cost)
    print("You don't have enough money!")
    print(f"You need {needed_money:.2f} leva!")