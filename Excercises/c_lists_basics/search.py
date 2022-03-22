number = int(input())
word = input()

strings = []

for i in range(number):
    current_string = input()
    strings.append(current_string)

filtered = []
for string in strings:
    if word in string:
        filtered.append(string)

print(strings)
print(filtered)