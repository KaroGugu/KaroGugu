numbers_list = [int(num) for num in input().split(' ')]

average = sum(numbers_list) / len(numbers_list)
numbers_list.sort(reverse=True)

result = ''
for index in range(len(numbers_list)):
    if numbers_list[index] > average:
        result += str(numbers_list[index]) + ' '
    else:
        break
    if index == 4:
        break

if result == '':
    result = 'No'

print(result)