month = input()                  # May, June, July, August, September, October
number_of_nights = int(input())

price_of_studio = 0
price_of_apartment = 0

if month == "May" or month == "October":
    price_of_studio += 50.00
    price_of_apartment += 65.00
    rent_of_studio = price_of_studio * number_of_nights
    rent_of_apartment = price_of_apartment * number_of_nights
    if number_of_nights > 7:
        if number_of_nights > 14:
            rent_of_studio *= 0.70               # 30% намаление
            rent_of_apartment *= 0.90            # 10% намаление
        elif number_of_nights > 7:
            rent_of_studio *= 0.95                   #  5% намаление

elif month == "June" or month == "September":
    price_of_studio += 75.20
    price_of_apartment += 68.70
    rent_of_studio = price_of_studio * number_of_nights
    rent_of_apartment = price_of_apartment * number_of_nights
    if number_of_nights > 14:
        rent_of_studio *= 0.80                  # 20% намаление
        rent_of_apartment *= 0.90

elif month == "July" or month == "August":
    price_of_studio += 76
    price_of_apartment += 77
    rent_of_studio = price_of_studio * number_of_nights
    rent_of_apartment = price_of_apartment * number_of_nights
    if number_of_nights > 14:
        rent_of_apartment *= 0.90

print(f"Apartment: {rent_of_apartment:.2f} lv.")
print(f"Studio: {rent_of_studio:.2f} lv.")