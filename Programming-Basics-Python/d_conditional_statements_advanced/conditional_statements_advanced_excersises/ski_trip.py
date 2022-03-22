number_of_days = int(input())
type_of_room = input()
feedback = input()

number_of_nights = number_of_days - 1

price_of_room_for_one_person = 18.00
price_of_apartment = 25.00
price_of_president_apartment = 35.00

if type_of_room == "room for one person":
    rent = number_of_nights * price_of_room_for_one_person
    if feedback == "positive":
        discount = 0.25 * rent
        rent += discount
    elif feedback == "negative":
        rent -= 0.10

if type_of_room == "apartment":
    rent = number_of_nights * price_of_apartment
    if number_of_nights <= 10:
        discount = 0.30 * rent
        rent -= discount
    elif 10 < number_of_nights <= 15:
        discount = 0.35 * rent
        rent -= discount
    elif number_of_nights > 15:
        discount = 0.50 * rent
        rent -= discount

    if feedback == "positive":
        discount = 0.25 * rent
        rent += discount
    elif feedback == "negative":
        discount = 0.10 * rent
        rent -= discount

if type_of_room == "president apartment":
    rent = number_of_nights * price_of_president_apartment
    if number_of_nights <= 10:
        discount = 0.10 * rent
        rent -= discount
    elif 10 < number_of_nights <= 15:
        discount = 0.15 * rent
        rent -= discount
    elif number_of_nights > 15:
        discount = 0.20 * rent
        rent -= discount

    if feedback == "positive":
        discount = 0.25 * rent
        rent += discount
    elif feedback == "negative":
        discount = 0.10 * rent
        rent -= discount

print(f"{rent:.2f}")