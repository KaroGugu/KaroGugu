import re

text = input()

# pattern_cool_threshold = r"\d+"

numbers = [int(el) for el in re.findall(r"\d", text)]
cool_threshold = 1

for num in numbers:
    cool_threshold *= num
    # cool_threshold = reduce(lambda x,y: x * y, numbers)

pattern_emoji = r"(::|\*\*)[A-Z][a-z]{2,}\1"
matches_emoji = re.finditer(pattern_emoji, text)
cool_emojis = []
emojis_count = 0

for match in matches_emoji:
    emoji = match.group()  # ::Smiley::
    emoji_without_surrounding = emoji.replace(emoji[0], "")  # Smiley
    emoji_coolness = sum([ord(el) for el in emoji_without_surrounding])  # sum [83, 109, 105, 108, 101, 121] = 627
    if emoji_coolness >= cool_threshold:
        cool_emojis.append(emoji)
    emojis_count += 1

print(f"Cool threshold: {cool_threshold}")
print(f"{emojis_count} emojis found in the text. The cool ones are:")
for emo in cool_emojis:
    print(emo)