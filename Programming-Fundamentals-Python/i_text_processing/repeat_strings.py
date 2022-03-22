words = input().split(' ')  # reads a sequence of strings, separated by a single space

final_string = ''

for word in words:  # Each string should be repeated N times
    final_string += word * len(word)  # N is the length of the string

print(final_string)