from tkinter import *

root = Tk()
root.title("Welcome")
root.geometry('400x100')

label = Label(root, text="This is Karolina's first GUI Application with tkinter")
label.pack()  # label.grid() - a geometry manager which keeps the label in the desired location inside the window


def clicked():
    label.configure(text="Gugudis", fg="dark blue")


button = Button(root, text="Click here to know my family name", fg="dark red", command=clicked)
button.pack()  # button.grid(column=1, row=0)  # change button grid location to column 2 as Entry() will be column 1


root.mainloop()
