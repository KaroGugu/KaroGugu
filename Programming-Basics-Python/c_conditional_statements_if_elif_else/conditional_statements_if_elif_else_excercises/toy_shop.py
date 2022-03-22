price_trip = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_cars = int(input())

price_of_puzzle = 2.60
price_of_doll = 3
price_of_bear = 4.10
price_of_minion = 8.20
price_of_car = 2

number_of_all_toys = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_cars
price_order = number_of_puzzles * price_of_puzzle + number_of_dolls * price_of_doll + number_of_bears * price_of_bear \
              + number_of_minions * price_of_minion + number_of_cars * price_of_car
rent = price_order * 0.1

if number_of_all_toys >= 50:
    price_order = price_order - (price_order * 0.25)                  # price_order -= price_order * 0.25
    rent = price_order * 0.1

money_for_trip = price_order - rent
left_money = abs(price_trip - money_for_trip)

if money_for_trip >= price_trip:
    print(f'Yes! {left_money:.2f} lv left.')

else:
    print(f'Not enough money! {left_money:.2f} lv needed.')