elements = input().split(" ")   # a single line containing some food (keys) and quantities (values) - separated by space
dictionary = {}

for i in range(0, len(elements), 2):  # key-value pairs, we can use a for-loop with step 2
    key = elements[i]
    value = elements[i + 1]
    dictionary[key] = int(value)  # the value must be an integer (since it is a quantity).

print(dictionary)