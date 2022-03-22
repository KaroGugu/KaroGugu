first_number = int(input())
second_number = int(input())

first_string = str(first_number)       # първата, втората, третата и четвъртата цифра от първото четирицифрено число
second_string = str(second_number)     # първата, втората, третата и четвъртата цифра от второто четирицифрено число

a1, b1, c1, d1 = int(first_string[0]), int(first_string[1]), int(first_string[2]), int(first_string[3])
a2, b2, c2, d2 = int(second_string[0]), int(second_string[1]), int(second_string[2]), int(second_string[3])

for a in range(a1, a2 + 1):
    # първата цифра от първото число като начална стойност, и от първата цифра от второто число като крайна стойност
    if a % 2 != 0:                                   # НЕ съдържат четни цифри в себе си
        for b in range(b1, b2 + 1):
            if b % 2 != 0:                           # НЕ съдържат четни цифри в себе си
                for c in range(c1, c2 + 1):
                    if c % 2 != 0:                   # НЕ съдържат четни цифри в себе си
                        for d in range(d1, d2 + 1):
                            if d % 2 != 0:           # НЕ съдържат четни цифри в себе си
                                print(a, b, c, d, sep="", end = " ")