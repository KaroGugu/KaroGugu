items = input().split("|")
budget = int(input())

profit = 0
new_item_prices = []
data_prices_as_string = []

for item in items:
    current_item_info = item.split("->")
    type_of_product = current_item_info[0]
    price_of_product = float(current_item_info[1])
    condition = False

    if type_of_product == "Clothes":
        if price_of_product <= 50:
            condition = True

    elif type_of_product == "Shoes":
        if price_of_product <= 35:
            condition = True


    elif type_of_product == "Accessories":
        if price_of_product <= 20.50:
            condition = True

    if condition:
        if budget >= price_of_product:
            budget -= price_of_product
            profit += price_of_product * 0.40
            new_price = price_of_product + (price_of_product * 0.40)
            new_item_prices.append(new_price)
            data_prices_as_string.append(f"{new_price:.2f}")

print(" ".join(data_prices_as_string))
print(f"Profit: {profit:.2f}")

total_sum = budget + sum(new_item_prices)
if total_sum >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")