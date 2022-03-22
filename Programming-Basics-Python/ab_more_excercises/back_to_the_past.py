money_heritage = float(input())
years_living = int(input())

start_year = 1800
age_ivan = 18 - 1

money_spent = 0

for year in range(1800, years_living + 1):
    if year % 2 == 0:
        money_heritage -= 12000
    elif year % 2 == 1:
        age_ivan += 2
        money_spent = (age_ivan * 50)
        money_heritage -= 12000 + money_spent

if money_heritage >= 0:
    print(f"Yes! He will live a carefree life and will have {money_heritage:.2f} dollars left.")
else:
    difference = abs(money_heritage)
    print(f"He will need {difference:.2f} dollars to survive.")