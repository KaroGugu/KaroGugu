first_list = input().split(", ")
second_list = input().split(", ")

substring = []

for word in first_list:
    for words in second_list:
        if word in words and not word in substring:
            substring.append(word)

print(substring)