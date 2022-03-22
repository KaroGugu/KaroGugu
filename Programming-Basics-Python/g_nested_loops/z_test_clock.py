from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Digital clock")
app_window.geometry("420x159")
app_window.resizable(1,1)

text_font = ("Boulder", 68, "bold")
background = "#0f0f0f"
foreground = "#f00a0a"
border_widt = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_widt)
label.grid(row=0, column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()