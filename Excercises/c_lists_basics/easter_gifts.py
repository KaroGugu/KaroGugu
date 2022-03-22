gifts = input().split(" ")

command = input()

while command != 'No Money':
    message = command.split(" ")
    command = message[0]
    the_gift = message[1]

    if command == 'OutOfStock':
        for index, current_gift in enumerate(gifts):
            if current_gift == the_gift:
                gifts[index] = 'None'

    elif command == 'Required':
        index = int(message[2])
        if 0 <= index < len(gifts):
            gifts[index] = the_gift

    elif command == 'JustInCase':
        gifts[-1] = the_gift

    command = input()

while 'None' in gifts:
    gifts.remove('None')

print(' '.join(gifts))