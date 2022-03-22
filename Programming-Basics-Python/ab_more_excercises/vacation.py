budget = float(input())
season = input()

price_of_hotel = 0
place = ""
country = ""

if season == "Summer":
    if budget <= 1000:
        place = "Camp"
        country = "Alaska"
        price_of_hotel = 0.65 * budget

    elif budget > 1000 and budget <= 3000:
        place = "Hut"
        country = "Alaska"
        price_of_hotel = 0.80 * budget

    elif budget > 3000:
        place = "Hotel"
        country = "Alaska"
        price_of_hotel = 0.90 * budget

if season == "Winter":
    if budget <= 1000:
        place = "Camp"
        country = "Morocco"
        price_of_hotel = 0.45 * budget

    elif budget > 1000 and budget <= 3000:
        place = "Hut"
        country = "Morocco"
        price_of_hotel = 0.60 * budget

    elif budget > 3000:
        place = "Hotel"
        country = "Morocco"
        price_of_hotel = 0.90 * budget

print(f"{country} - {place} - {price_of_hotel:.2f}")