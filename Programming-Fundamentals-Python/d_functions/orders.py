def total_price_of_order():
    product = input()
    number_of_products = int(input())

    price = 0

    if product == "coffee":
        price += 1.50
    elif product == "water":
        price += 1
    elif product == "coke":
        price += 1.40
    elif product == "snacks":
        price += 2.00

    total_sum = price * number_of_products
    print(f"{total_sum:.2f}")

total_price_of_order()