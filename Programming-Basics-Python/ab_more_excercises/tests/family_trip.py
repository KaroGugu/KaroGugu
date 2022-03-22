budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_others = float(input())     # процента от бюджета са предвидили за допълнителни разходи

all_nights_price = 0

if nights > 7:                          # ако броят на нощувките е по-голям от 7, цената за нощувка се намаля с 5%
    price_per_night -= 0.05 * price_per_night

all_nights_price += nights * price_per_night

price_others = (percent_others / 100) * budget   # допълнителни разходи

total_money_needed = all_nights_price + price_others

difference = abs(budget - total_money_needed)
if total_money_needed <= budget:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")