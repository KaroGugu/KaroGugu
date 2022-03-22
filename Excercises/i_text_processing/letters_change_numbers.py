string = input().split()

alphabet = "abcdefghijklmnopqrstuvwxyz"
num_character = lambda char: alphabet.index(char.lower()) + 1  # letter's position in the alphabet

total_sum = 0

for word in string:
    first_char = num_character(word[0])  # letter in front of the number
    last_char = num_character(word[-1])  # letter after of the number
    number_in_word = int(word[1:-1])

    if word[0].isupper():  # divide the number by the letter's position in the alphabet
        number_in_word /= first_char
    elif word[0].islower():
        number_in_word *= first_char  # multiply the number with the letter's position in the alphabet

    if word[-1].isupper():  # subtract its position from the resulting number
        number_in_word -= last_char
    elif word[-1].islower():  # add its position to the resulting number
        number_in_word += last_char

    total_sum += number_in_word

print(f"{total_sum:.2f}")



