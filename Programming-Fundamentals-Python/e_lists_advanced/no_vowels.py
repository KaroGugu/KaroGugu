vowels = ["a", "e", "o", "u", "i"]

text = input()

# result = []
# for element in text:
#     if element.lower() not in vowels:
#         result.append(element)
#
# print("".join(result))

result = [element for element in text if element.lower() not in vowels]
print("".join(result))