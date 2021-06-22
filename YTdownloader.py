from pytube import YouTube
import sys
import math

def handleProgress(stream, chunk, bytes_remaining):     #function that displays the progress of the download
    total = size    #store the total file size
    percent = math.floor(((total - bytes_remaining)/total) * 100)
    full = "#" * percent 
    empty = "-" * (100 - percent)
    msg = "DOWNLOADING:[{}{}]"
    #print(empty)
    print(msg.format(full, empty),end='\r')  #compare the total minus the complete to the total

def handleComplete(stream, file_path):  #Displays a message to show that the download has finnished
    print("DOWNLOADING:[####################################################################################################]")

if len(sys.argv) == 2:  #if there is only 1 argument (argument 0 is the name of the script)   
    try:    
        yt = YouTube(sys.argv[1],on_progress_callback=handleProgress,on_complete_callback=handleComplete).streams.first()
        size = yt.filesize
        yt.download()    #try to lookup the first argument as a YT URL, select the first strem and download it
    except: 
        print("failed to download") #if the download fails tell the user and exit
elif len(sys.argv) >2:  #if the argument list is longer than 1
    isHelperArgument = False    #Signals that the argument was intended to be used with another
    try:
        yt = YouTube(sys.argv[1], on_progress_callback=handleProgress, on_complete_callback=handleComplete)   #First, try to lookup the URL given in the first argument
        stream = yt.streams.first() #by default, just get the first steam in the list
        name = yt.title + ".mp4"    #by default the name is the title of the video
        path = "."
    except:
        print("invalid URL")    #if it fails the URL is invalid

    offset = 0  
    argument = 0    #keeps track of the argument number
    for i in sys.argv:  #for every argument
        if offset < 2:  #skip the first 2 argument (0 is the script name and 1 is the URL)
            offset +=1
            argument +=1
            continue
        if i == "-a":   #the -a is used to get an audio only stream   
            stream = yt.streams.get_audio_only()    #get the highest quality audio stream and overwrite the stream variable
        elif i == "-v": # -v signals for the stream to be video only
            stream = yt.streams.filter(only_video=True).first()     #filter the streams to only have audio only streams, then select the first one
        elif i =="-n":  #-n is followed by the desired name for the file
            name = sys.argv[argument+1] #store the next argument as the new name
            isHelperArgument = True #signal that the next argument is a helper
        elif i == "-p": # -p sets the path where the video should be downloaded
            path = sys.argv[argument + 1]   #Set the path the the next argument
            isHelperArgument = True         #Signal that the next argument is a helper
        else:   #if the argument is not a -option
            if isHelperArgument:    #check to see if is a helper   
                isHelperArgument = False
            else:
                print("Invalid Arguments")  #if is is not a helper then exit
                break
        argument += 1
    try:
        size = stream.filesize
        stream.download(output_path = path, filename = name)
    except:
        print("failed to Download")
else:
    print("Invalid Arguments")