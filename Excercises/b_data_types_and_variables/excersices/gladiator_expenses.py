lost_fights_counter = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())

gladiador_expenses = 0
shield_counter = 0

for lost in range(1, lost_fights_counter + 1):

    if lost % 2 == 0:
        gladiador_expenses += helmet_price

    if lost % 3 == 0:
        gladiador_expenses += sword_price
        if lost % 2 == 0:
            gladiador_expenses += shield_price
            shield_counter += 1

            if shield_counter == 2:
                gladiador_expenses += armour_price
                shield_counter = 0

print(f"Gladiator expenses: {gladiador_expenses:.2f} aureus")