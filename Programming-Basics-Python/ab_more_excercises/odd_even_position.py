import sys

numbers = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize

even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for number in range(numbers):
    current_number = float(input())

    if (number + 1) % 2 == 0:                  # четни и нечетни позиции
        even_sum += current_number
        if current_number < even_min:
            even_min = current_number
        if current_number > even_max:
            even_max = current_number
    else:
        odd_sum += current_number
        if current_number < odd_min:
            odd_min = current_number
        if current_number > odd_max:
            odd_max = current_number

if numbers > 0:
    odd_min_text = f"{odd_min:.2f}"
    odd_max_text = f"{odd_max:.2f}"
else:
    odd_min_text = "No"
    odd_max_text = "No"

if numbers > 1:
    even_min_text = f"{even_min:.2f}"
    even_max_text = f"{even_max:.2f}"
else:
    even_min_text = "No"
    even_max_text = "No"

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={odd_min_text},")
print(f"OddMax={odd_max_text},")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={even_min_text},")
print(f"EvenMax={even_max_text}")