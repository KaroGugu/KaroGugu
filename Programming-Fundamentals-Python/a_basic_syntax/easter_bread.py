budget = float(input())
one_kg_flour_price = float(input())

bread_counter = 0
color_eggs_counter = 0

eggs_price = one_kg_flour_price * 0.75
milk_price_per_bread = (one_kg_flour_price * 1.25) / 4     # 250 ml milk needed for one bread

one_bread_price = one_kg_flour_price + eggs_price + milk_price_per_bread

while budget - one_bread_price >= 0:
    budget -= one_bread_price
    bread_counter += 1
    color_eggs_counter += 3

    if bread_counter % 3 == 0:
        color_eggs_counter -= bread_counter - 2

print(f"You made {bread_counter} loaves of Easter bread! Now you have {color_eggs_counter} eggs and {budget:.2f}BGN left.")