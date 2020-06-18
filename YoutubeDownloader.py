# Youtube video downloader

import tkinter
from pytube import YouTube

def download():
    global entry1
    toDownload = entry1.get()
    #print(toDownload)
    youtube = YouTube(str(toDownload))
    videos = yt.get_videos()

    x = 1

    for i in videos:
        print(str(x)+"."+str(i))
        x= x+1

    n = int(input("Enter your choice"))
    vid = videos[n-1]

    destination = str(input("Enter your destination"))
    vid.downloaded(destination)
    print(yt.filename+"/n has been downloaded")
    
    entry1.delete(first=0, last=100)



root = tkinter.Tk()
root.title("Youtube Downloader")
root.geometry("400x100")


title = tkinter.Label(root, text="Youtube Video Downloader")
title.pack()

entry1 = tkinter.Entry(root)#, bd=5)
entry1.pack()

button1 = tkinter.Button(root, text="Download", fg="white", bg="red", command=download)
button1.pack()



root.mainloop()
