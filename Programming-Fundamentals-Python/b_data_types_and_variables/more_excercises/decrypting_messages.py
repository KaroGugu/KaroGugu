key = int(input())
number_of_lines = int(input())

decripted_message = ""

for line in range(number_of_lines):
    letter = input()
    new_message = ord(letter) + key
    decripted_message += chr(new_message)

print(decripted_message)