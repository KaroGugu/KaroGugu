budget = float(input())
number_of_statists = int(input())
price_one_dress = float(input())

decor = budget * 0.1          # budget * 10 / 100
dresses_price = number_of_statists * price_one_dress

if number_of_statists > 150:
    dresses_price *= 0.9                # dresses = dresses_price * 90 / 100
                                        # отстъпка за облеклото на стойност 10%
needed_money = decor + dresses_price
difference = abs(needed_money - budget)  # парите недостигащи за филма или оставащи като излишък

if needed_money > budget:
    print("Not enough money!")
    print (f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")                            # if budget >= needed money
    print(f"Wingard starts filming with {difference:.2f} leva left.")