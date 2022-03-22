number_of_lines = int(input())

opening_brackets_counter = 0
closing_brackets_counter = 0

is_balanced = True

for line in range(0, number_of_lines):
    symbol = input()

    if symbol == "(":
        opening_brackets_counter += 1

    elif symbol == ")":
        closing_brackets_counter += 1

    if closing_brackets_counter > opening_brackets_counter:
        is_balanced = False
        break

    elif opening_brackets_counter - 1 > closing_brackets_counter:
        is_balanced = False
        break

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")