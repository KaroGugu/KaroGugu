quantity = int(input())
days_left_to_Christmas = int(input())

total_cost = 0
total_spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
lights_price = 15

for current_day in range(1, days_left_to_Christmas + 1):
    if current_day % 11 == 0:
        quantity += 2      # increase the allowed quantity with 2 at the beginning of every eleventh day

    if current_day % 2 == 0:
        total_cost += ornament_set_price * quantity
        total_spirit += 5
    if current_day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garlands_price) * quantity
        total_spirit += 13
    if current_day % 5 == 0:
        total_cost += lights_price * quantity
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30

    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_garlands_price + lights_price

if days_left_to_Christmas % 10 == 0:  # last day is a tenth day
    total_spirit -= 30


print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")