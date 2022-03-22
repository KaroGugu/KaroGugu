price_party = float(input())
number_of_love_letters = int(input())
number_of_roses = int(input())
number_of_keyrings = int(input())
number_of_caricatures = int(input())
number_of_surprises = int(input())

sum_love_letters = number_of_love_letters * 0.60
sum_roses = number_of_roses * 7.20
sum_keyrings = number_of_keyrings * 3.60
sum_caricatures = number_of_caricatures * 18.20
sum_surprises = number_of_surprises * 22

total_sum = sum_love_letters + sum_roses + sum_keyrings + sum_caricatures + sum_surprises
total_number = number_of_love_letters + number_of_roses + number_of_keyrings + number_of_caricatures + number_of_surprises

if total_number >= 25:
    total_sum = total_sum - (0.35 * total_sum)

left_money = total_sum - (0.10 * total_sum)

diff = abs(left_money - price_party)
if left_money >= price_party:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")