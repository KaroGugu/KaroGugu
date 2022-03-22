number_of_people = int(input())
season = input()

price = 0

if number_of_people <= 5:
    if season == "spring":
        price += 50.00
    elif season == "summer":
        price += 48.50
    elif season == "autumn":
        price += 60.00
    elif season == "winter":
        price += 86.00

elif number_of_people > 5:
    if season == "spring":
        price += 48.00
    elif season == "summer":
        price += 45.00
    elif season == "autumn":
        price += 49.50
    elif season == "winter":
        price += 85.00

total_sum = number_of_people * price

if season == "summer":
    total_sum -= 0.15 * total_sum
elif season == "winter":
    total_sum += 0.08 * total_sum

print(f"{total_sum:.2f} leva.")