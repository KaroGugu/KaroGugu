price_over_20 = float(input())
luggage_kg = float(input())
days_till_departure = int(input())
luggage_num = int(input())

if luggage_kg < 10:
    price = price_over_20 / 5
elif 10 <= luggage_kg <= 20:
    price = price_over_20 / 2
else:
    price = price_over_20

if days_till_departure > 30:
    price = price + (price * 0.1)  # questionable
elif 7 <= days_till_departure <= 30:
    price = price + (price * 0.15)
elif days_till_departure < 7:
    price = price + (price * 0.4)

total_price_of_bags = price * luggage_num

print(f"The total price of bags is: {total_price_of_bags:.2f} lv.")