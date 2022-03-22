def grades():
    grade = float(input())
    word = ""
    if grade >= 2.00 and grade <= 2.99:
        word = "Fail"
    elif 3.00 <= grade <= 3.49:
        word = "Poor"
    elif 3.50 <= grade <= 4.49:
        word = "Good"
    elif 4.50 <= grade <= 5.49:
        word = "Very Good"
    elif 5.50 <= grade <= 6.00:
        word = "Excellent"

    print(word)

grades()