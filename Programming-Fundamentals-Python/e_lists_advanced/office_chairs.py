number_of_rooms = int(input())
free_chairs = 0

for room in range(1, number_of_rooms + 1):
    chairs_and_visitors = input().split(' ')
    chairs = int(len(chairs_and_visitors[0]))
    visitors = int(chairs_and_visitors[1])

    if chairs < visitors:
        print(f'{visitors - chairs} more chairs needed in room {room}')
        free_chairs -= visitors - chairs
    elif chairs >= visitors:
        free_chairs += chairs - visitors

if free_chairs >= 0:
    print(f'Game On, {free_chairs} free chairs left')
