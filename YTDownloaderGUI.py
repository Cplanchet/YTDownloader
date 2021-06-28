from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from pytube import *
from threading import *
import sys

def handleProgress(stream, chunk, bytes_remaining):     #Used to keep track of download progress and update the Progress Bar
    percent = ((total - bytes_remaining)/total)*100
    Progress["value"] = percent

def handleEnd(stream, file_path):      #Used to set the Progress Bar to full when the download completes
    Progress["value"] = 100

def onButtonPress():    #Handles the Download once the Button is presses (This function is called in a parallel thread)
    EnterButton["state"] = DISABLED     #Disable the button, entry, and checkbox
    UrlInput["state"] = DISABLED
    cb["state"] = DISABLED

    path = fd.asksaveasfilename()   #Display the File system and ask for the path and name to be chosen
    temp = path.split("/")  #Used to split the path from the name, starts by splitting the full path delineated on "/"
    path=""
    for i in range(len(temp) - 1):  #for all of the seperated strings except the last
        path = path + temp[i]   #add the string back into the path string
        path = path + "/"   #add the / back into the string
    last = len(temp)    #the last string is stored as the name
    fileName = temp[last-1]
    
    try:
        yt = YouTube(UrlInput.get(), on_progress_callback=handleProgress, on_complete_callback=handleEnd)   #Create a YouTube object with the entered URL
        global total
        if Checked.get() == 0:
            total = yt.streams.first().filesize     #if the does not want an audio only string, store the file size and download stream
            stream = yt.streams.first()
        else:
            total = yt.streams.get_audio_only().filesize    #if the user wants an audio only stream, record the filesize and download string
            stream = yt.streams.get_audio_only()
    except:
       mb.showerror("URL ERROR", "Invalid URL")     #For any failures enable all components and kill the thread
       EnterButton["state"] = NORMAL
       UrlInput["state"] = NORMAL
       cb["state"] = NORMAL
       sys.exit()
       
    
    try:
        stream.download(output_path=path, filename=fileName)    #Download the video
    except:
        mb.showerror("DOWNLOAD ERROR", "Failed to Download")
        EnterButton["state"] = NORMAL
        UrlInput["state"] = NORMAL
        cb["state"] = NORMAL
        sys.exit()

    mb.showinfo("Success", "Download Complete!")    #on success enable all components and kill the thread
    EnterButton["state"] = NORMAL
    UrlInput["state"] = NORMAL
    cb["state"] = NORMAL
    sys.exit()

def background():       #used to call the button handler using a new thread
    bt = Thread(target=onButtonPress)
    bt.start()
    
root = Tk()
root.title("YouTube Download Tool")
root.iconbitmap('res/YTDownloader_Icon.ico')

frame = Frame(root, pady= 10 ,padx= 50)
frame.pack()

frameBot = Frame(root, pady=5)
frameBot.pack(side=TOP)

pbFrame = Frame(root, pady = 15)
pbFrame.pack()

UrlLabel = Label(frame, text="URL")
UrlLabel.pack(side=LEFT)

UrlInput = Entry(frame, width=30)
UrlInput.pack(side=LEFT)

EnterButton = Button(frameBot, command= background, text = "Download as...")
EnterButton.pack(side=RIGHT)

Checked = IntVar()
cb = Checkbutton(frameBot, text="Audio Only", variable=Checked)
cb.pack(side=LEFT)

Progress = ttk.Progressbar(pbFrame, orient="horizontal", length=250, mode="determinate")
Progress.pack()

root.mainloop()