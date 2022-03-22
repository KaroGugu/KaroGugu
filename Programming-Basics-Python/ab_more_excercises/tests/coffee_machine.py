drink = input()
sugar = input()
number_of_drinks = int(input())

price = 0

if drink == "Espresso":
    if sugar == "Without":
        price += 0.90
    elif sugar == "Normal":
        price += 1
    elif sugar == "Extra":
        price += 1.20
elif drink == "Cappuccino":
    if sugar == "Without":
        price += 1.00
    elif sugar == "Normal":
        price += 1.20
    elif sugar == "Extra":
        price += 1.60
elif drink == "Tea":
    if sugar == "Without":
        price += 0.50
    elif sugar == "Normal":
        price += 0.60
    elif sugar == "Extra":
        price += 0.70

total_price = price * number_of_drinks

# Отстъпките се прилагат в реда на тяхното описване

if sugar == "Without":        # При избрана напитка без захар има 35% отстъпка
    total_price -= 0.35 * total_price

if drink == "Espresso":       # При избрана напитка "Espresso" и закупени поне 5 броя, има 25% отстъпка
    if number_of_drinks >= 5:
        total_price -= 0.25 * total_price

if total_price > 15:          # При сума надвишава 15 лева, 20% отстъпка от крайната цена
    total_price -= 0.20 * total_price

print(f"You bought {number_of_drinks} cups of {drink} for {total_price:.2f} lv.")