type_of_final = input()
type_of_ticket = input()
number_of_tickets = int(input())
picture = input()

price_ticket = 0

if type_of_final == "Quarter final":
    if type_of_ticket == "Standard":
        price_ticket += 55.50
    elif type_of_ticket == "Premium":
        price_ticket += 105.20
    elif type_of_ticket == "VIP":
        price_ticket += 118.90

elif type_of_final == "Semi final":
    if type_of_ticket == "Standard":
        price_ticket += 75.88
    elif type_of_ticket == "Premium":
        price_ticket += 125.22
    elif type_of_ticket == "VIP":
        price_ticket += 300.40


elif type_of_final == "Final":
    if type_of_ticket == "Standard":
        price_ticket += 110.10
    elif type_of_ticket == "Premium":
        price_ticket += 160.66
    elif type_of_ticket == "VIP":
        price_ticket += 400

total_price = price_ticket * number_of_tickets
if total_price > 2500 and total_price <= 4000:
    total_price = total_price - (0.10 * total_price)
elif total_price > 4000:
    total_price = total_price - (0.25 * total_price)

if picture == "Y":   # При избрана опция за снимки с трофея, цената се начислява след изчисляването на отстъпките.
    price_photos = number_of_tickets * 40
    total_price += price_photos
    if total_price > 4000:                                # Над 4000 лири има безплатни снимки с трофея
        total_price -= price_photos                       # към цената не добавяме допълнителна такса

elif picture == "N":
    total_price = total_price

print(f"{total_price:.2f}")