list_of_numbers = input().split()
numbers_to_remove = int(input())

final_list = []

for num in list_of_numbers:
    final_list.append(int(num))

for _ in range(numbers_to_remove):
    final_list.remove(min(final_list))


print(final_list)
