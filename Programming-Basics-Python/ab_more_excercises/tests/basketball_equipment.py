tax = int(input())

price_shoes = tax - (0.40 * tax)
price_dress = price_shoes - (0.20 * price_shoes)
price_ball = price_dress / 4
price_accessories = price_ball / 5

total_price = tax + price_shoes + price_dress + price_ball + price_accessories

print(f"{total_price:.2f}")