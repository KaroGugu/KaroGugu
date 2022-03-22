fruit = input()
day_of_week = input()
number = float(input())

if day_of_week in "Monday, Tuesday, Wednesday, Thursday, Friday":
    price = 0
    if fruit == "banana":
        price = 2.50
        total_price = price * number
        print(round(total_price, 2))
    elif fruit == "apple":
        price = 1.20
        total_price = price * number
        print(round(total_price, 2))
    elif fruit == "orange":
        price = 0.85
        total_price = price * number
        print(round(total_price, 2))
    elif fruit == "grapefruit":
        price = 1.45
        total_price = price * number
        print(round(total_price, 2))
    elif fruit == "kiwi":
        price = 2.70
        total_price = price * number
        print(round(total_price, 2))
    elif fruit == "pineapple":
        price = 5.50
        total_price = price * number
        print(round(total_price, 2))
    elif fruit == "grapes":
        price = 3.85
        total_price = price * number
        print(round(total_price, 2))
    else:
        print("error")


elif day_of_week in "Saturday, Sunday":
    price = 0
    if fruit == "banana":
        price = 2.70
        total_price = price * number
        print(round(total_price, 2))
    elif fruit == "apple":
        price = 1.25
        total_price = price * number
        print(round(total_price, 2))
    elif fruit == "orange":
        price = 0.90
        total_price = price * number
        print(round(total_price, 2))
    elif fruit == "grapefruit":
        price = 1.60
        total_price = price * number
        print(round(total_price, 2))
    elif fruit == "kiwi":
        price = 3.00
        total_price = price * number
        print(round(total_price, 2))
    elif fruit == "pineapple":
        price = 5.60
        total_price = price * number
        print(round(total_price, 2))
    elif fruit == "grapes":
        price = 4.20
        total_price = price * number
        print(round(total_price, 2))
    else:
        print("error")
else:
    print("error")