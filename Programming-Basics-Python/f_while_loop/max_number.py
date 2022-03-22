import sys

max_number = -sys.maxsize           # 92233720368... = max number in Python

while True:
    number = input()              # защото по някое време ще получим вход "Stop"

    if number == "Stop":
        break
    elif int(number) > max_number:   # преобразуваме думата в число
        max_number = int(number)

print(max_number)