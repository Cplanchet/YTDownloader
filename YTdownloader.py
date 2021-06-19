from pytube import YouTube
import sys

if len(sys.argv) == 2:   
    try:
        YouTube(sys.argv[1]).streams.first().download()
        print("download Complete")
    except:
        print("failed to download")
elif len(sys.argv) == 3:
    if sys.argv[2] == "-a":
        try:
            YouTube(sys.argv[1]).streams.get_audio_only().download()
            print("Download Complete")
        except:
            print("Failed to Download")    
    else:
        print("Invalid Arguments")
else:
    print("Invalid Arguments")