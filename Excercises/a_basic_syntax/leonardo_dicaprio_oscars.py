number = int(input())

text = ""
if number == 88:
    text = "Leo finally won the Oscar! Leo is happy"
elif number == 86:
    text = "Not even for Wolf of Wall Street?!"
elif number < 88:
    text = "When will you give Leo an Oscar?"
else:
    text = "Leo got one already!"

print(text)