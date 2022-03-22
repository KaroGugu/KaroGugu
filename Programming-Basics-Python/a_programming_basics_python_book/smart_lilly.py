age_lilly = int(input())
price_washing_machine = float(input())
price_toy = int(input())

number_of_toys = 0
saved_money = 0
money_for_birthday = 0

for birthdays in range(1, age_lilly + 1):
    if birthdays % 2 == 0:
        money_for_birthday += 10  # За втория рожден ден получава 10.00 лв., като сумата се
        # увеличава с 10.00 лв. за всеки следващ четен рожден ден
        saved_money += money_for_birthday - 1      # Братът взима по 1.00 лев от парите всяка четна година

    else:
        number_of_toys += 1

saved_money += number_of_toys * price_toy

difference = abs(price_washing_machine - saved_money)
if saved_money >= price_washing_machine:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")