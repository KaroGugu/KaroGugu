
# речниците в Пайтън - създаващ по 1 речник за цифрите ,десетиците и още един за числата между 11 и 19 включително

numbers_1_to_10 ={0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                  9: "nine", 10: 'ten'}
nembers_11_to_19={11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
                  17: "seventeen", 18: "eighteen", 19: "nineteen"}
nembers_20_to_100={20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
                   80: "eighty", 90: "ninety", 100: "one hundred"}
number = int(input())

if number >= 0 and number <= 10:
    print(numbers_1_to_10.get(number))
elif number >10 and number <= 19:
    print(nembers_11_to_19.get(number))
elif number >19 and number <=100:
    if number % 10 == 0:
        print(nembers_20_to_100.get(number))
    else:
        print(nembers_20_to_100.get((number // 10) * 10), numbers_1_to_10.get(number % 10))
# Ако е по голямо от 19 ,правиш проверка дали ако се раздели на 10 остатъка е нула.
# Ако е нула - вадиш числото от речника с десетиците
# Ако има остатък вадиш едновременно първо от десетиците ,после от цифрите и принтираш резултата