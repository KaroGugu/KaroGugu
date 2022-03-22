number_of_juniors = int(input())
number_of_seniors = int(input())
type_of_race = input()

tax_juniors = 0
tax_seniors = 0
total_sum = 0
expenses = 0.05

if type_of_race == "trail":
    tax_juniors = 5.50
    tax_seniors = 7
    total_sum = number_of_seniors * tax_seniors + number_of_juniors * tax_juniors
    expenses *= total_sum

elif type_of_race == "cross-country":
    tax_juniors = 8
    tax_seniors = 9.50
    if (number_of_seniors + number_of_juniors) >= 50:
        tax_juniors = tax_juniors - (tax_juniors * 0.25)
        tax_seniors = tax_seniors - (tax_seniors * 0.25)
        total_sum = number_of_seniors * tax_seniors + number_of_juniors * tax_juniors
        expenses *= total_sum
    else:
        total_sum = number_of_seniors * tax_seniors + number_of_juniors * tax_juniors
        expenses *= total_sum

elif type_of_race == "downhill":
    tax_juniors = 12.25
    tax_seniors = 13.75
    total_sum = number_of_juniors * tax_juniors + number_of_seniors * tax_seniors
    expenses *= total_sum

elif type_of_race == "road":
    tax_juniors = 20
    tax_seniors = 21.50
    total_sum = number_of_juniors * tax_juniors + number_of_seniors * tax_seniors
    expenses *= total_sum

money_for_donation = total_sum - expenses

print(f"{money_for_donation:.2f}")