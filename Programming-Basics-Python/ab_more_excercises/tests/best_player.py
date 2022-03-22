import sys

max_goals = 0
name_of_player = ''
count = 0
for i in range(sys.maxsize):
    string = input()
    if string == 'END':  # ако е въведен 'END' прекъсва цикъла
        break
    num_of_goals = int(input())
    if num_of_goals > max_goals:  # проверява за максимален брой голове и присвоява име на играча
        name_of_player = string
        max_goals = num_of_goals
    if num_of_goals >= 10:  # ако са повече от 10 отпечатва каквото трябва и спира програмата
        print(f'{name_of_player} is the best player!')
        print(f'He has scored {max_goals} goals and made a hat-trick !!!')
        sys.exit()
    if num_of_goals == max_goals:  # проверява колко пъти имаме еднакъв брой голове
        count += 1
        if count == 1:  # присвоява име на играча който е въведен пръв с този брой голове /в условието не е описано това
            # виджа се в таблицата с изходите...доста се полутах,докато забележа тази подробност/
            max_goals = num_of_goals
            name_of_player = string

if max_goals >= 3:
    print(f'{name_of_player} is the best player!')
    print(f'He has scored {max_goals} goals and made a hat-trick !!!')
else:
    print(f'{name_of_player} is the best player!')
    print(f'He has scored {max_goals} goals.')