budget = float(input())
number_video_cards = int(input())
number_procesurs = int(input())
number_ram_memmories = int(input())

price_video_cards = number_video_cards * 250
price_procecesure = (price_video_cards * 0.35) * number_procesurs
price_ram_memmory = (price_video_cards * 0.10) * number_ram_memmories

total_price = price_video_cards + price_procecesure + price_ram_memmory

if number_video_cards > number_procesurs:
    discount = total_price - (total_price * 0.15)
    money_left = (budget - discount)

else:
    money_left = abs(budget - total_price)

if budget >= total_price:
    print(f'You have {abs(money_left):.2f} leva left!')

else:
    print(f'Not enough money! You need {abs(money_left):.2f} leva more!')