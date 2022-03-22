flower = input()
number_of_flowers = int(input())
budget = int(input())

price_of_roses = 5
price_of_dahlias = 3.80
price_of_tulips = 2.80
price_of_narcissus = 3
price_of_gladiolus = 2.50

total_price = 0
if flower == "Roses":
    if number_of_flowers > 80:
        total_price = (number_of_flowers * price_of_roses) * 0.90     # 10% отстъпка от крайната цена
    else:
        total_price = number_of_flowers * price_of_roses

elif flower == "Dahlias":
    if number_of_flowers > 90:
        total_price = (number_of_flowers * price_of_dahlias) * 0.85   # 15% отстъпка
    else:
        total_price = number_of_flowers * price_of_dahlias

elif flower == "Tulips":
    if number_of_flowers > 80:
        total_price = (number_of_flowers * price_of_tulips) * 0.85   # 15% отстъпка
    else:
        total_price = number_of_flowers * price_of_tulips

elif flower == "Narcissus":
    if number_of_flowers < 120:                                   # цената се оскъпява с 15%
        total_price = (number_of_flowers * price_of_narcissus) + (0.15 * number_of_flowers * price_of_narcissus)
    else:
        total_price = number_of_flowers * price_of_narcissus

elif flower == "Gladiolus":                                       # цената се оскъпява с 15%
    if number_of_flowers < 80:
        total_price = (number_of_flowers * price_of_gladiolus) + (0.20 * number_of_flowers * price_of_gladiolus)
    else:
        total_price = number_of_flowers * price_of_gladiolus


difference = abs(total_price - budget)
if total_price > budget:
    print(f"Not enough money, you need {difference:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower} and {difference:.2f} leva left.")