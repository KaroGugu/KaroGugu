text = input()
text = text.lower()

needed_words = ["sand", "water", "fish", "sun"]
counter = 0

for word in needed_words:
    if word in text:
        word_counter_in_text = text.count(word)
        counter += word_counter_in_text

print(counter)