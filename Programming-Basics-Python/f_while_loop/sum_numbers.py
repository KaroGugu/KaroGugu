number = int(input())

sum = 0

while sum < number:                  # докато тяхната сума стане по-голяма или равна на първоначалното число
    current_number = int(input())    # всеки следващ ред цели числа
    sum += current_number

print(sum)