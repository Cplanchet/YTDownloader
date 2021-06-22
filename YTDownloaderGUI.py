from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from pytube import *
import sys

def onButtonPress():
    EnterButton["state"] = DISABLED
    path = fd.asksaveasfilename()
    temp = path.split("/")
    path=""
    for i in range(len(temp) - 1):
        path = path + temp[i]
        path = path + "/"
    last = len(temp)
    fileName = temp[last-1]
    try:
        yt = YouTube(UrlInput.get())
    except:
       mb.showerror("URL ERROR", "Invalid URL")
       sys.exit()
    
    try:
        yt.streams.first().download(output_path=path, filename=fileName)
    except:
        mb.showerror("DOWNLOAD ERROR", "Failed to Download")
        sys.exit()

    mb.showinfo("Success", "Download Complete!")
    sys.exit()
root = Tk()
root.title("YouTube Download Tool")
root.iconbitmap('res/YTDownloader_Icon.ico')

frame = Frame(root, pady=20, padx= 100)
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

