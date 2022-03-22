x = float(input())            # височината на къщата
y = float(input())            # дължината на страничната стена
h = float(input())            # височината на триъгълната стена на прокрива

#  за стените се използва зелена боя, а за покрива – червена

# стените
# Предната и задната стена са квадрати със страна X
front_wall = x * x         # 6 * 6 = 36
back_wall = x * x           # 6 * 6 = 36
door = 1.2 * 2
front_and_back_wall = 2 * (front_wall) - door              # 2*36 - 2.4
# Страничните стени са правоъгълници със страни „x“ и „y
side_wall = x * y
window = 1.5 * 1.5
two_side_walls = 2 * side_wall - 2 * window

# покрив
# 2 правоъгълника със страни „x“ и „y“
# 2 равностранни триъгълника със страна „x“ и височина „h“
ceiling = (2 * (x * y)) + (2 * (x*h / 2))

# Разхода на зелената боя е 1 литър за 3.4 м2, а на червената – 1 литър за 4.3 м2.
liters_green_paint = (front_and_back_wall + two_side_walls) / 3.4
red_paint = ceiling / 4.3

print (f'{liters_green_paint:.2f}')
print (f'{red_paint:.2f}')
