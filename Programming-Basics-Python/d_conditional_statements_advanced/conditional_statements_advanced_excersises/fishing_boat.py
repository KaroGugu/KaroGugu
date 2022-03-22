budget = int(input())
season = input()
number_of_fishermen = int(input())

rent_of_boat = 0

if season == "Spring":
    rent_of_boat = 3000
elif season == "Summer" or season == "Autumn":
    rent_of_boat = 4200
elif season == "Winter":                       # else:
    rent_of_boat = 2600

# discount
if number_of_fishermen <= 6:
    rent_of_boat *= 0.9                    # 10 % discount         => rent_of_boat = 100 - 10 = 90%
elif 6 < number_of_fishermen <= 11:        # 7 <= number_of_fishermen <= 11
    rent_of_boat *= 0.85                    # 15 % discount         => rent_of_boat = 100 - 15 = 85%
elif number_of_fishermen >= 12:           # else:
    rent_of_boat *= 0.75                    # 25 % discount         => rent_of_boat = 100 - 25 = 75%

# additional_discount = 0.05    # except in autumn
if season != "Autumn" and number_of_fishermen % 2 == 0:        # if not season == "Autumn"
    rent_of_boat *= 0.95                    # 5% discount    => rent_of_boat = 100 - 5 = 95%

difference = abs(budget - rent_of_boat)
if budget >= rent_of_boat:
    print(f"Yes! You have {difference:.2f} leva left.")
elif budget < rent_of_boat:
    print(f"Not enough money! You need {difference:.2f} leva.")