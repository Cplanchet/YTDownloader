from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from pytube import *

def onButtonPress():
    path = fd.asksaveasfilename()
    
    temp = path.split("/")
    last = len(temp)
    fileName = temp[last-1]
    print(fileName)

    print(UrlInput.get())
    try:
        pass
        yt = YouTube(UrlInput.get())
    except:
       pass
       mb.showerror("Ru Ro Raggy", "Invalid URL")



root = Tk()
root.title("YouTube Download Tool")
root.iconbitmap('res/YTDownloader_Icon.ico')

frame = Frame(root)
frame.pack()

frameBot = Frame(root)
frameBot.pack(side=BOTTOM)

UrlLabel = Label(frame, text="URL")
UrlLabel.pack(side=LEFT)

UrlInput = Entry(frame)
UrlInput.pack(side=LEFT)

EnterButton = Button(frameBot, command= onButtonPress, text = "Download as...")
EnterButton.pack()
root.mainloop()

