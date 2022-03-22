price_without_taxes = 0

command = input()
while command != "special" and command != "regular":
    price_of_part = float(command)

    if price_of_part >= 0:
        price_without_taxes += price_of_part
    else:
        print("Invalid price!")

    if command == "special" or command == "regular":
        break

    command = input()

if price_without_taxes > 0:
    taxes = price_without_taxes * 0.20
    total_price = taxes + price_without_taxes
    if command == 'special':
        total_price -= 0.10 * total_price

    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {price_without_taxes:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f"Total price: {total_price:.2f}$")

else:
    print("Invalid order!")