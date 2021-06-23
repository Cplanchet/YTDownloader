from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from pytube import *
from threading import *
import sys


def handleProgress(stream, chunk, bytes_remaining):
    percent = ((total - bytes_remaining)/total)*100
    Progress["value"] = percent
def handleEnd(stream, file_path):
    print("data")
    Progress["value"] = 100
def onButtonPress():
    EnterButton["state"] = DISABLED
    UrlInput["state"] = DISABLED
    path = fd.asksaveasfilename()
    temp = path.split("/")
    path=""
    for i in range(len(temp) - 1):
        path = path + temp[i]
        path = path + "/"
    last = len(temp)
    fileName = temp[last-1]
    try:
        yt = YouTube(UrlInput.get(), on_progress_callback=handleProgress, on_complete_callback=handleEnd)
        global total
        total = yt.streams.first().filesize
    except:
       mb.showerror("URL ERROR", "Invalid URL")
       EnterButton["state"] = NORMAL
       UrlInput["state"] = NORMAL
       sys.exit()
       
    
    try:
        yt.streams.first().download(output_path=path, filename=fileName)
    except:
        mb.showerror("DOWNLOAD ERROR", "Failed to Download")
        EnterButton["state"] = NORMAL
        UrlInput["state"] = NORMAL
        sys.exit()

    mb.showinfo("Success", "Download Complete!")
    EnterButton["state"] = NORMAL
    UrlInput["state"] = NORMAL
    sys.exit()

def background():
    bt = Thread(target=onButtonPress)
    bt.start()
root = Tk()
root.title("YouTube Download Tool")
root.iconbitmap('res/YTDownloader_Icon.ico')

frame = Frame(root, pady=20, padx= 50)
frame.pack()

frameBot = Frame(root)
frameBot.pack(side=BOTTOM)

UrlLabel = Label(frame, text="URL")
UrlLabel.pack(side=LEFT)

UrlInput = Entry(frame, width=30)
UrlInput.pack(side=LEFT)

EnterButton = Button(frameBot, command= background, text = "Download as...")
EnterButton.pack()

Progress = ttk.Progressbar(root, orient="horizontal", length=250, mode="determinate")
Progress.pack(side=BOTTOM)

root.mainloop()

