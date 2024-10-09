import shutil, os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from shutil import *
from PIL import ImageTk, Image

#declare vars
imgname = r"4weirdegg.png"
srcpath = r"from/"
directory1 = r"dir1/"
directory2 = r"dir2/"
fileList : list[str]

#declare gui vars
root : Tk
img : PhotoImage
newImg : PhotoImage
image : Label
title : Label
frame : Frame
dir1 : Button
dir2 : Button



def moveFile(directory) :
    shutil.move(srcpath + imgname, directory + imgname)
    if(changeImageFile()) :
        changeImage()

def defineDirectories() :
    global directory1, directory2 

    directory1 = filedialog.askdirectory(parent = root, initialdir="/", title = "Directory 1")
    directory2 = filedialog.askdirectory(parent = root, initialdir="/", title = "Directory 2")

def defineSource() :
    global srcpath

    srcpath = filedialog.askdirectorya(parent = root, initialdir = "/", title= "Source")

def changeImageFile() -> bool:
    global imgname
    fileList.remove(fileList[0])
    if(len(fileList) > 0) :
        imgname = os.listdir(srcpath)[0]
        print(imgname)
        return True
    return False
        
def changeImage() :
    global img, image
    img = ImageTk.PhotoImage(Image.open(srcpath + imgname))
    image = ttk.Label(frame, image = img)
    image.pack()
    

def init() :
    #init vars
    global fileList, root, img, image, title, frame, dir1, dir2

    fileList = os.listdir(srcpath)
    changeImageFile()

    #root and main frame
    root = Tk()
    root.title("Image Sorter")
    frame = ttk.Frame(root, padding="1 1 1 1", width = 100, height = 100)
    frame.grid(column=0, row=0, sticky=(N,W,E,S))
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight=1)

    #title
    title = ttk.Label(frame, text="Image Sorter")
    title.grid(column = 1, row = 0, columnspan = 2)

    #image
    img = ImageTk.PhotoImage(Image.open(srcpath+imgname))
    image = ttk.Label(frame, image = img)
    image.grid(column = 1, row=1, columnspan = 2)

    #directory buttons
    dir1 = ttk.Button(frame, text = directory1, command= lambda : moveFile(directory1))
    dir1.grid(column = 1, row = 2)
    dir2 = ttk.Button(frame, text = directory2, command = lambda : moveFile(directory2))
    dir2.grid(column = 2, row = 2)

def main() :
    init()
    root.mainloop()


if __name__ == "__main__" : 
    main()