target = float(input())
cocktail_name = input()
income, difference = 0, 0
is_target_reached = False

while cocktail_name != "Party!":
    number_of_cocktails = int(input())

    cocktail_price = len(cocktail_name)             # цената на един коктейл е дължината неговото име
    total_price = number_of_cocktails * cocktail_price

    if total_price % 2 != 0:     # Ако цената на една поръчка е нечетно число, има 25% отстъпка от цената на поръчката
        total_price *= 0.75

    income += total_price
    difference = abs(target - income)

    if income >= target:
        print("Target acquired.")
        print(f"Club income - {income:.2f} leva.")
        is_target_reached = True
        break

    cocktail_name = input()

if is_target_reached is False:
    print(f"We need {difference:.2f} leva more.")
    print(f"Club income - {income:.2f} leva.")