number_of_chrysanthemums = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
holiday_yes_or_no = input()

total_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips

if season == "Spring" or season == "Summer":
    price = (number_of_chrysanthemums * 2) + (number_of_roses * 4.10) + (number_of_tulips * 2.50)
    if holiday_yes_or_no == "Y":
        price += price * 0.15
    if number_of_tulips > 7:
        price -= price * 0.05
    if total_flowers > 20:
        price -= price * 0.20
    price += 2

elif season == "Autumn" or season == "Winter":
    price = (number_of_chrysanthemums * 3.75) + (number_of_roses * 4.50) + (number_of_tulips * 4.15)
    if holiday_yes_or_no == "Y":
        price += price * 0.15
    if number_of_roses >= 10 and season == "Winter":
        price -= price * 0.10
    if total_flowers > 20:
        price -= price * 0.20
    price += 2

print(f"{price:.2f}")