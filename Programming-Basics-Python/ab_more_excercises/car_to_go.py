budget = float(input())
season = input()

class_of_car = ""
type_of_car = ""
price_of_car = 0

if budget <= 100:
    class_of_car = "Economy class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price_of_car = 0.35 * budget

    elif season == "Winter":
        type_of_car = "Jeep"
        price_of_car = 0.65 * budget

elif budget > 100 and budget <= 500:
    class_of_car = "Compact class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price_of_car = 0.45 * budget
    elif season == "Winter":
        type_of_car = "Jeep"
        price_of_car = 0.80 * budget

else:                    # elif budget > 500:
    class_of_car = "Luxury class"
    type_of_car = "Jeep"
    price_of_car = 0.90 * budget

print(class_of_car)
print(f"{type_of_car} - {price_of_car:.2f}")
