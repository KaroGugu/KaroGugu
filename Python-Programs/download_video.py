"""
from pytube import YouTube

link = input("Please enter the URL of the video you want to download: ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()

stream.download()

"""


# from pytube import YouTube
# YouTube(input("Enter video URL: ")).streams.get_highest_resolution().download()



from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Youtube video downloader")


Label(root, text="Download Youtube video for free", font='san-serif 13 bold').pack()
link = StringVar()

Label(root, text="Paste the video link here:", font='san-serif 15 bold').place(x=150, y=55)
link_enter = Entry(root, width=70, textvariable=link).place(x=30, y=85)

Button(root, text='Download', font='san-serif 10 bold', bg='light blue', padx=2, command="download").place(x=100, y=150)


def download():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text="Downloaded", font="arial 15").place(x=100, y=120)


root.mainloop()
