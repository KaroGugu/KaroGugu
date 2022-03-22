age_lilly = int(input())
price_of_washing_machine = float(input())
price_of_toy = int(input())

money_on_birthday = 0
total_money = 0
total_number_of_toys = 0

for current_age in range(1, age_lilly + 1):
    if current_age % 2 != 0:                 # нечетните рождени дни
        total_number_of_toys += 1
    else:                                    # четните рождени дни
        money_on_birthday += 10              # втория рожден ден получава 10.00 лв, като сумата се увеличава с 10.00 лв
        total_money += money_on_birthday - 1 # Братът на Лили, в годините, които тя получава пари, взима по 1.00 лев

total_money += total_number_of_toys * price_of_toy         # продала играчките получени през годините, всяка за P лева
                                                           # и добавила сумата към спестените пари

difference = abs(total_money - price_of_washing_machine)

if total_money >= price_of_washing_machine:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")