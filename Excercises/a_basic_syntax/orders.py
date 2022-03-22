number_of_orders = int(input())

total_price = 0

for order in range(1, number_of_orders + 1):
    capsules_price = float(input())
    days = int(input())
    number_of_capsules = int(input())

    price_order = capsules_price * number_of_capsules * days
    print(f"The price for the coffee is: ${price_order:.2f}")
    total_price += price_order

print(f"Total: ${total_price:.2f}")