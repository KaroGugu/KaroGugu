length = float(input())       # from m to sm
width = float(input())         # from m to sm

length *= 100
width *= 100

# 1 rabotno mqsto = 70 * 120 sm
door = 1
katedra = 2
corridor = 100

rows = (width - corridor) // 70
sides = length // 120

seats = (rows * sides) - 3

print(int(seats))

