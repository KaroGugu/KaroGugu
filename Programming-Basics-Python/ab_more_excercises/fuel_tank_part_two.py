type_of_fuel = input()
liters_fuel = int(input())
club_card = input()

price = 0

if type_of_fuel == "Gasoline":
    price = 2.22 * liters_fuel
    if club_card == "Yes":
        price = (2.22 - 0.18) * liters_fuel
elif type_of_fuel == "Diesel":
    price = 2.33 * liters_fuel
    if club_card == "Yes":
        price = (2.33 - 0.12) * liters_fuel
elif type_of_fuel == "Gas":
    price = 0.93 * liters_fuel
    if club_card == "Yes":
        price = (0.93 - 0.08) * liters_fuel

if 20 < liters_fuel <= 25:
    price *= 0.92                               # 8 процента отстъпка от крайната цена
elif liters_fuel > 25:
    price *= 0.90                               # 10 процента отстъпка от крайната цена

print(f"{price:.2f} lv.")