initial_energy = int(input())
command = input()

battles_won_counter = 0
game_won = True


while not command == 'End of battle':
    distance_to_enemy = int(command)

    if distance_to_enemy > initial_energy:
        game_won = False
        break
    elif distance_to_enemy <= initial_energy:
        initial_energy -= distance_to_enemy
    battles_won_counter += 1

    if battles_won_counter % 3 == 0:
        initial_energy += battles_won_counter

    command = input()

if game_won:
    print(f"Won battles: {battles_won_counter}. Energy left: {initial_energy}")
else:
    print(f"Not enough energy! Game ends with {battles_won_counter} won battles and {initial_energy} energy")