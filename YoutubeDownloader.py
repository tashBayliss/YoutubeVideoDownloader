# Youtube video downloader

import tkinter

def download():
    global entry1
    toDownload = entry1.get()
    print(toDownload)



root = tkinter.Tk()

title = tkinter.Label(root, text="Youtube Video Downloader")
title.pack()

entry1 = tkinter.Entry(root)#, bd=5)
entry1.pack()

button1 = tkinter.Button(root, text="Download", fg="white", bg="red", command=download)
button1.pack()



root.mainloop()
