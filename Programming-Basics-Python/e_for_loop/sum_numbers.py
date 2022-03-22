number = int(input())                         # показва броя числата/ интеракции,които ще върти

total_sum = 0

for _ in range(number):             # взимаме броя числа, които са динамични / всеки път са различни на брой
                                # _ ни показва,че не я взимаме под внимание; може да бъде и буква
    current_num = int(input())
    total_sum += current_num                  # total_sum = total_sum + current_num

print(total_sum)