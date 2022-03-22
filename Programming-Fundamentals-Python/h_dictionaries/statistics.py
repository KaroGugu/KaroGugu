products = {}

command = input()
while command != "statistics":
    current_command = command.split(": ")
    product = current_command[0]
    quantity = int(current_command[1])

    if product not in products:
        products[product] = 0   # we make sure that the product will exist before we add the quantity
    products[product] += quantity

    command = input()

print("Products in stock:")

for (product, quantity) in products.items():   # [print(f" - {product}: {quantity}") for (product, quantity in products]
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
