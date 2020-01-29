#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

from tkinter import *
from functools import partial
import os
import messageFrame, toolBarFrame, statusBarFrame
import generalInfo
import os
from PIL import ImageTk, Image
from tkinter import filedialog

class sourceFrame():
    def __init__(self, master):

        LoadImage = Image.open("../images/add-document.png")
        LoadImage = LoadImage.resize((25, 25), Image.ANTIALIAS)
        self.LoadPhoto = ImageTk.PhotoImage(LoadImage)


        self.fileList = os.listdir("../")

        self.sourceFrame_0 = Frame(master, width = master.winfo_screenwidth() * 0.4, height = master.winfo_screenheight() * 0.4, bg="#B3B3D3")
        self.sourceFrame_0.pack_propagate(0)
        self.sourceFrame_0.pack(padx=4, pady=4)

        #Directory Window
        self.LeftFrame = Canvas(self.sourceFrame_0, width=master.winfo_screenwidth() * 0.1, height=master.winfo_screenheight() * 0.4, bg="#C2BEB0")
        self.LeftFrame.grid(row=0, column=0)
        self.LeftFrame.pack_propagate(0) 
        self.LeftLabel_0 = Label(self.LeftFrame, text= "Directory", font=("Courier", 14), bg="#C2BEB0", anchor='nw')
        self.LeftLabel_0.pack(padx=4, pady=4)


        self.listBox = Listbox(self.LeftFrame, height=27, bg="#C2BEB0")
        self.listBox.pack(padx=4, pady=4, fill='both')
        
        for item in self.fileList:
            self.listBox.insert(END, item)

        # Source Design Window
        self.RightFrame = Frame(self.sourceFrame_0, width=master.winfo_screenwidth() * 0.3, height=master.winfo_screenheight() * 0.4, bg="#B3B3D3")
        self.RightFrame.grid(row=0, column=1)
        self.RightFrame.pack_propagate(0)
        
        self.RightTopFrame = Frame(self.RightFrame, width= master.winfo_screenwidth() * 0.3, height=32, bg="#B3B3B3")
        self.RightTopFrame.pack(side=TOP, fill=X)
        self.RightTopFrame.pack_propagate(0)

        self.RightLabel_0 = Label(self.RightTopFrame, text= "Design Window", font=("Courier", 14), bg="#B3B3C2", anchor='center')
        self.RightLabel_0.grid(row=0, column=0)

        self.AddDesign = Button(self.RightTopFrame, image=self.LoadPhoto, command = self.fileBrowser)
        self.AddDesign.grid(row=0, column=1, padx=(4, 4), pady=(4, 4))


        self.RightBottomFrame = Frame(self.RightFrame, width= master.winfo_screenwidth() * 0.3, height=400, bg="#B3B3D0")
        self.RightBottomFrame.pack(fill='both')



    def fileBrowser(self):
        self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        self.PathLabel = Label(self.RightBottomFrame, text = "")
        self.PathLabel.grid(column = 1, row = 2)
        self.PathLabel.configure(text = self.filename)
        print("Open file ",self.filename)

