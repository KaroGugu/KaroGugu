initial_health = 100
initial_bitcoins = 0

dungeon_rooms = input().split('|')

health = initial_health
best_room = 0
is_dead = False


for i in range(len(dungeon_rooms)):
    best_room += 1
    command = dungeon_rooms[i]
    data = command.split()

    if data[0] == 'potion':
        number = int(data[1])
        if health + number > initial_health:
            number = initial_health - health
            health = initial_health
        else:
            health += number
        print(f'You healed for {number} hp.')
        print(f'Current health: {health} hp.')

    elif data[0] == 'chest':
        amount = int(data[1])
        print(f'You found {amount} bitcoins.')
        initial_bitcoins += amount
    else:
        monster = data[0]
        attack = int(data[1])
        health -= attack
        if health > 0:
            print(f'You slayed {monster}.')
        else:
            print(f'You died! Killed by {monster}.')
            print(f'Best room: {best_room}')
            is_dead = True
            break

if not is_dead:
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {health}")