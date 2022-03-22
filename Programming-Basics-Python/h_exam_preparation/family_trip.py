budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_others = int(input())      # / 100

costs = 0

# Трябва да се има предвид, че ако броят на нощувките е по-голям от 7, цената за нощувка се намаля с 5%.
if number_of_nights > 7:
    price_per_night -= price_per_night * 0.05

costs = number_of_nights * price_per_night
# cost_others = budget * (percent_others / 100)
# costs += cost_others
costs += budget * (percent_others / 100)

diff = abs(budget - costs)
if budget >= costs:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")