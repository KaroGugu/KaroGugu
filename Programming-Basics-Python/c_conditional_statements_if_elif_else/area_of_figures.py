from math import pi

figure = input()

if figure == 'square':
    number_1 = float(input())
    area = number_1 * number_1
    print(round (area, 3))

elif figure == 'rectangle':
    number_1 = float(input())
    number_2 = float(input())
    area = number_1 * number_2
    print(round (area, 3))

elif figure == 'circle':
    number_1 = float(input())
    area = pi * (number_1 ** 2)
    print(round(area, 3))

elif figure == 'triangle':
    number_1 = float(input())
    number_2 = float(input())
    area = number_1 * number_2 / 2
    print(round (area, 3))