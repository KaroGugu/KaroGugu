start_char = input()
end_char = input()
random_string = input()

sum_of_ascii = 0

for char in random_string:   # all characters in the random string
    if ord(start_char) < ord(char) < ord(end_char):  #  the ASCII values of the two given characters
        sum_of_ascii += ord(char)

print(sum_of_ascii)
