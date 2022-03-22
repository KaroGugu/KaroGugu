season = input()
type_of_group = input()
number_of_students = int(input())
number_of_nights = int(input())

price_of_night = 0
sport = ""

if season == "Winter":
    if type_of_group == "girls" or type_of_group == "boys":
        price_of_night = 9.60
    else:
        price_of_night = 10
    if type_of_group == "girls":
        sport = "Gymnastics"
    elif type_of_group == "boys":
        sport = "Judo"
    else:
        sport = "Ski"

elif season == "Spring":
    if type_of_group == "girls" or type_of_group == "boys":
        price_of_night = 7.20
    else:
        price_of_night = 9.50
    if type_of_group == "girls":
        sport = "Athletics"
    elif type_of_group == "boys":
        sport = "Tennis"
    else:
        sport = "Cycling"

elif season == "Summer":
    if type_of_group == "mixed":
        price_of_night = 20
    else:
        price_of_night = 15
    if type_of_group == "mixed":
        sport = "Swimming"
    elif type_of_group == "boys":
        sport = "Football"
    else:
        sport = "Volleyball"

price_of_holiday = number_of_nights * price_of_night * number_of_students

if number_of_students >= 50:
    price_of_holiday -= price_of_holiday * 0.50
    # discount = price_of_holiday * 0.50
    # price_of_holiday = price_of_holiday - discount

elif number_of_students >= 20 < 50:
    price_of_holiday -= price_of_holiday * 0.15
elif number_of_students >=10 < 20:
    price_of_holiday -= price_of_holiday * 0.05

print(f"{sport} {price_of_holiday:.2f} lv.")