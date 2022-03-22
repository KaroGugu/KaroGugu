word = input()
counter = int(input())

repeat_word = lambda word, counter: word * counter
result = repeat_word(word, counter)

print(result)