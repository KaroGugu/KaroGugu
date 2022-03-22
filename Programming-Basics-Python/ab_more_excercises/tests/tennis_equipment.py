from math import ceil
price_tennis_racket = float(input())
number_tennis_rackets = int(input())
number_of_shoes = int(input())

price_shoes = price_tennis_racket / 6
price_racket_and_shoes = price_tennis_racket * number_tennis_rackets + price_shoes * number_of_shoes
price_other_stuff = 0.20 * price_racket_and_shoes
total_price = price_racket_and_shoes + price_other_stuff

paid_by_Djokovic = total_price / 8
paid_by_sponsors = total_price * (7/8)

print(f"Price to be paid by Djokovic {int(paid_by_Djokovic)}") # закръглена към по-малкото цяло число
print(f"Price to be paid by sponsors {ceil(paid_by_sponsors)}") # закръглена към по-малкото цяло число