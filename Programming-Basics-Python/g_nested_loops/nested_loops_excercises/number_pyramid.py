number = int(input())

current_number = 1
is_current_bigger_than_number = False

for row in range(1, number + 1):                  # колко реда да се отпечатат
    for column in range(1, row + 1):          # колко числа се принтират на съответния ред

        if current_number > number:
            is_current_bigger_than_number = True
            break
        print(f"{current_number} ", end='')
        current_number += 1
    if is_current_bigger_than_number:
         break
    print()