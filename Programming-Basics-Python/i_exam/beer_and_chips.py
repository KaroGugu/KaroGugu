from math import ceil

name_of_person = input()
budget = float(input())
number_of_bottles_beer = int(input())
number_of_chips_packets = int(input())

price_beer = 1.20
total_price_beer = price_beer * number_of_bottles_beer

price_chips = total_price_beer * 0.45
total_price_chips = price_chips * number_of_chips_packets
total_price_chips = ceil(total_price_chips)

total_money_spent = total_price_beer + total_price_chips

diff = abs(total_money_spent - budget)
if total_money_spent <= budget:
    print(f"{name_of_person} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name_of_person} needs {diff:.2f} more leva!")