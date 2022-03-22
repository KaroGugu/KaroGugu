rent_hall = int(input())

price_statue = rent_hall - (0.30 * rent_hall)
price_food = price_statue - (0.15 * price_statue)
price_sound = price_food / 2

total_price = rent_hall + price_statue + price_food + price_sound

print(f"{total_price:.2f}")