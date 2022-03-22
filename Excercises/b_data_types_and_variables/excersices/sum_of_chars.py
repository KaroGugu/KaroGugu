number_of_lines = int(input())

sum_of_chars = 0

for line in range(0, number_of_lines):
    letter = input()
    sum_of_chars += ord(letter)

print(f"The sum equals: {sum_of_chars}")