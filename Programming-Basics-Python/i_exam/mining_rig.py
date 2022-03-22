from math import ceil

price_video_card = int(input())
price_prehodnik = int(input())
price_electricity = float(input())
profit_from_a_card_per_day = float(input())

number_of_video_cards = 13
number_or_prehodnik = 13
price_other = 1000

total_price_card = price_video_card * number_of_video_cards
total_price_prehodnik = price_prehodnik * number_or_prehodnik

total_money_spent = total_price_card + total_price_prehodnik + price_other

profit_per_day = profit_from_a_card_per_day - price_electricity
total_profit_from_card_per_day = number_of_video_cards * profit_per_day

days_for_return = total_money_spent / total_profit_from_card_per_day

print(total_money_spent)
print(ceil(days_for_return))
