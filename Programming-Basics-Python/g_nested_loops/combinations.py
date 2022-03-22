number = int(input())

combination = 0
for n1 in range(number + 1):
    for n2 in range(number + 1):
        for n3 in range(number + 1):
            if n1 + n2 + n3 == number:                 # 0, 0, 0
                                                       # 0, 0, 1
                                                       # 0, 0, 2
                                                       # ..
                                                       # if (0+ 0+ 0) == number
                                                       # if (0+ 0+ 25) == number
                                                       # print (combination)
                combination += 1
print(combination)