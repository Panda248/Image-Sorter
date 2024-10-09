import shutil, os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from shutil import *
from PIL import ImageTk, Image, ImageFile

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
dirBrowse : Button
srcBrowse : Button
skip : Button


def moveFile(directory) :
    shutil.move(srcpath + imgname, directory + imgname)
    fileList.remove(fileList[0])
    if(changeImageFile()) :
        changeImage()

def defineDirectories() :
    global directory1, directory2, dir1, dir2

    directory1 = filedialog.askdirectory(parent = root, initialdir="/", title = "Directory 1") + "/"
    directory2 = filedialog.askdirectory(parent = root, initialdir="/", title = "Directory 2") + "/"
    
    dir1.configure(text = directory1)
    dir1.text = directory1
    dir2.configure(text= directory2)
    dir2.text = directory2
    

def defineSource() :
    global srcpath, fileList, srcBrowse

    srcpath = filedialog.askdirectory(parent = root, initialdir = "/", title= "Source") + "/"
    fileList = os.listdir(srcpath)
    
    srcBrowse.configure(text = srcpath)
    srcBrowse.text = srcpath
    
    changeImageFile()
    changeImage()

def changeImageFile() -> bool:
    global imgname
    while(not (fileList[0].endswith(".png") or fileList[0].endswith(".PNG") or fileList[0].endswith(".jpg") or fileList[0].endswith(".JPG"))) :
        fileList.remove(fileList[0])
    
    if(len(fileList) > 0) :
        imgname = fileList[0]
        print(srcpath + imgname)
        return True
    return False
        
def changeImage() :
    global img, image
    img = ImageTk.PhotoImage(Image.open(srcpath + imgname).resize((500,500)))
    image.configure(image=img)
    image.image = img

def skipImage() :
    fileList.remove(fileList[0])
    if(changeImageFile()) :
        changeImage()
    
def init() :
    #init vars
    global fileList, root, img, image, title, frame, dir1, dir2, dirBrowse, srcBrowse, skip

    ImageFile.LOAD_TRUNCATED_IMAGES = True
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
    title.grid(column = 1, row = 0, columnspan = 3)

    #image
    img = ImageTk.PhotoImage(Image.open(srcpath+imgname).resize((500,500)))
    image = ttk.Label(frame, image = img)
    image.grid(column = 1, row=1, columnspan = 3)

    #sort buttons
    dir1 = ttk.Button(frame, text = directory1, command= lambda : moveFile(directory1))
    dir1.grid(column = 1, row = 2)
    dir2 = ttk.Button(frame, text = directory2, command = lambda : moveFile(directory2))
    dir2.grid(column = 3, row = 2)
    
    #skip button
    skip = ttk.Button(frame, text = "Skip", command = skipImage)
    skip.grid(column = 2, row = 2)
    
    #source and directory browser buttons
    dirBrowse = ttk.Button(frame, text = "Select Directories", command = defineDirectories)
    dirBrowse.grid(row = 0, column = 0)
    srcBrowse = ttk.Button(frame, text = srcpath, command = defineSource)
    srcBrowse.grid(row = 0, column = 4)
    

def main() :
    init()
    root.mainloop()


if __name__ == "__main__" : 
    main()