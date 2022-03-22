budget = float(input())
number_of_people = int(input())
price_clothes = float(input())

price_decor = 0.10 * budget

if number_of_people > 150:
    price_clothes -= 0.10 * price_clothes

total_money = price_decor + (price_clothes * number_of_people)

difference = abs(total_money - budget)
if total_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")