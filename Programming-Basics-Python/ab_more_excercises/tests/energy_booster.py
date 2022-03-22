fruit = input()
size = input()
number_of_packets = int(input())

price = 0

if fruit == "Watermelon":
    if size == "small":               # 2 бр. енергиен гел В разфасовката
        price += 2 * 56                   # цената за брой енергиен гел
    elif size == "big":               # 5 бр. енергиен гел В разфасовката
        price += 5 * 28.70
elif fruit == "Mango":
    if size == "small":
        price += 2 * 36.66
    elif size == "big":
        price += 5 * 19.60
elif fruit == "Pineapple":
    if size == "small":
        price += 2 * 42.10
    elif size == "big":
        price += 5 * 24.80
elif fruit == "Raspberry":
    if size == "small":
        price += 2 * 20
    elif size == "big":
        price += 5 * 15.20

total_price_of_order = number_of_packets * price

if total_price_of_order >= 400 and total_price_of_order <= 1000:
    total_price_of_order = total_price_of_order - (total_price_of_order * 0.15)        # 15% отстъпка
elif total_price_of_order > 1000:
    total_price_of_order -= total_price_of_order * 0.50

print(f"{total_price_of_order:.2f} lv.")