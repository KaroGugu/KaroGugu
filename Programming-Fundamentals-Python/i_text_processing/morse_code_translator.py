# https://morsecode.world/international/translator.html

morse_code = [str(word).strip() for word in input().split(' | ')]

result = []

morse_code_dict = { '.-':'A', '-...':'B',
                    '-.-.':'C', '-..':'D', '.':'E',
                    '..-.':'F', '--.':'G', '....':'H',
                    '..':'I', '.---':'J', '-.-':'K',
                    '.-..':'L', '--':'M', '-.':'N',
                    '---':'O', '.--.':'P', '--.-':'Q',
                    '.-.':'R', '...':'S', '-':'T',
                    '..-':'U', '...-':'V', '.--':'W',
                    '-..-':'X', '-.--':'Y', '--..':'Z'}

for morse_word in morse_code:
    english_word = ''.join([morse_code_dict[morse_char] for morse_char in morse_word.split(' ')])
    result.append(english_word)


print(' '.join(result))