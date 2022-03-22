data = input()

products = {}

while not data == "buy":
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:   # If the product doesn't exist yet, add it with its starting quantity
        products[name] = {"price": price, "quantity": quantity}   # nested dictionary == key

    else:
        products[name]["quantity"] += quantity   # increases its quantity by the input quantity
        products[name]["price"] = price  # if its price is different, replace the price as well

    data = input()

for key,value in products.items():
    result = value["price"] * value["quantity"]  # the total price of each product
    print(f"{key} -> {result:.2f}")