word = input()
repeat = int(input())

def repeat_string(word, repeat):
    word_repeated = word * repeat
    return word_repeated

print(repeat_string(word, repeat))