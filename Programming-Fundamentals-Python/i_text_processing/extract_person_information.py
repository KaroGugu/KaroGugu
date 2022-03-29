number_of_lines = int(input())

for line in range(number_of_lines):
    text = input()
    symbol1 = text.find('@')
    symbol2 = text.find('|')
    symbol3 = text.find('#')
    symbol4 = text.find('*')

    name = text[symbol1 + 1:symbol2]
    age = text[symbol3 + 1:symbol4]

    print(f'{name} is {age} years old.')