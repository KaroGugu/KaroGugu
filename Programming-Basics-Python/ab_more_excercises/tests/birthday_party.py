rent_hall = float(input())

cake = 0.20 * rent_hall               # 20% от наема
drinks = cake - (0.45 * cake)         # 45% по-малко от тази на тортата
animator = rent_hall / 3

needed_money = rent_hall + cake + drinks + animator
print(needed_money)