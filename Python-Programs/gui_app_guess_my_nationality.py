from tkinter import *

root = Tk()
root.title("Welcome")
root.geometry('400x100')

label = Label(root, text="This is Karolina's first GUI Application with tkinter")
label.pack()

def nationality():
    label.configure(text="My nationality is: Bulgarian", fg="dark blue")

question = Entry(root, width=10)   # create a text box for user input
question.pack()

res = "Can you guess my nationality? Enter your choice here:"
label.configure(text=res)

button_for_nationality = Button(root, text="Click here to see if your answer is correct", fg="dark red", command=nationality)
button_for_nationality.pack()

root.mainloop()
