season = input()
kilometers_per_month = float(input())

money_per_kilometer = 0
# 1 working season = 4 months

if season == "Spring" or season == "Autumn":
    if kilometers_per_month <= 5000:
        money_per_kilometer = 0.75
    elif kilometers_per_month > 5000 and kilometers_per_month <= 10000:
        money_per_kilometer = 0.95
    else:
        money_per_kilometer = 1.45

elif season == "Summer":
    if kilometers_per_month <= 5000:
        money_per_kilometer = 0.90
    elif kilometers_per_month > 5000 and kilometers_per_month <= 10000:
        money_per_kilometer = 1.10
    else:
        money_per_kilometer = 1.45

elif season == "Winter":
    if kilometers_per_month <= 5000:
        money_per_kilometer = 1.05
    elif kilometers_per_month > 5000 and kilometers_per_month <= 10000:
        money_per_kilometer = 1.25
    else:
        money_per_kilometer = 1.45

salary_for_month = kilometers_per_month * money_per_kilometer
taxes = 0.10 * salary_for_month
salary_for_working_season = 4 * (salary_for_month - taxes)

print(f"{salary_for_working_season:.2f}")