text = input()

capital_letters = [index for index, chr in enumerate(text) if chr.isupper()]

print(capital_letters)