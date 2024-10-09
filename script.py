import shutil
from tkinter import *
from tkinter import ttk
from shutil import *


imgname = r"4weirdegg.png"
srcpath = r"from/"
directory1 = r"dir1/"
directory2 = r"dir2/"


def moveFile(directory) :
    shutil.move(srcpath + imgname, directory + imgname)


root = Tk()
root.title("Image Sorter")
frame = ttk.Frame(root, padding="1 1 1 1", width = 100, height = 100)
frame.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight=1)

title = ttk.Label(frame, text="Image Sorter", )
img = PhotoImage(file=srcpath + imgname)
image = ttk.Label(frame, image = img).grid(column = 1, row=1, columnspan = 2)
button = ttk.Button(frame, text = directory1, command= lambda : moveFile(directory1)).grid(column = 1, row = 2)
button2 = ttk.Button(frame, text = directory2, command = lambda : moveFile(directory2)).grid(column = 2, row = 2)


root.mainloop()