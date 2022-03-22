number_of_cities = int(input())

day_profit = 0
total_profit = 0

for city in range(1, number_of_cities + 1):
    name_of_city = input()
    owner_income = float(input())
    owner_expenses = float(input())

    day_profit = owner_income - owner_expenses

    if city % 3 == 0:
        owner_expenses += 0.50 * owner_expenses
        day_profit = owner_income - owner_expenses

    if city % 5 == 0:
        owner_income -= owner_income * 0.10
        day_profit = owner_income - owner_expenses

    total_profit += day_profit
    print(f"In {name_of_city} Burger Bus earned {day_profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")