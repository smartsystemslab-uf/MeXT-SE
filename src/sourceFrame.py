#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

from tkinter import *
#from tkinter.ttk import *
import xml.dom.minidom
from functools import partial
import os
import messageFrame, toolBarFrame, statusBarFrame
import generalInfo
import os
from PIL import ImageTk, Image
from tkinter import filedialog
import IPparse, DesignTree

class sourceFrame():
    def __init__(self, master):

        LoadImage = Image.open("../images/add-document.png")
        LoadImage = LoadImage.resize((25, 25), Image.ANTIALIAS)
        self.LoadPhoto = ImageTk.PhotoImage(LoadImage)


        self.fileList = os.listdir("../design-folder/")

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
        self.treeData = DesignTree.DesignTree(self.RightBottomFrame)



    def fileBrowser(self):
        try:
            self.filename = filedialog.askopenfilename(initialdir = "../",title = "Select file",filetypes = (("design files","*.xml"),("all files","*.*")))

            print("Open file ", self.filename)
            self.treeData.generateTree(self.filename)
        except:
            print("Error: File path not given")
    
    def newCompFunc(self):
        self.compWin = Toplevel()
        self.compWin.wm_title("New Component...")
        self.compNameLabel = Label(self.compWin, text="Component Name : ")
        self.compNameLabel.grid(row=0, column=0, padx=(10, 10), pady=(8, 8))
        self.compNameEntry = Entry(self.compWin)
        self.compNameEntry.grid(row=0, column=1, padx=(10, 10), pady=(8, 8))

        self.configLabel1 = Label(self.compWin, text="Configuration 1 : ")
        self.configLabel1.grid(row=1, column=0, padx=(2, 10), pady=(8, 0))

        self.valLabel1 = Label(self.compWin, text="Value : ")
        self.valLabel1.grid(row=1, column=1, padx=(10, 10), pady=(8, 0))

        self.configName1 = Entry(self.compWin)
        self.configName1.grid(row=2, column=0, padx=(10, 10), pady=(4, 4))

        self.configVal1 = Entry(self.compWin)
        self.configVal1.grid(row=2, column=1, padx=(10, 10), pady=(4, 4))

        self.cofigLabel2 = Label(self.compWin, text="Configuration 2 : ")
        self.cofigLabel2.grid(row=3, column=0, padx=(2, 10), pady=(8, 0))
        
        self.valLabel2 = Label(self.compWin, text="Value : ")
        self.valLabel2.grid(row=3, column=1, padx=(10, 10), pady=(8, 0))

        self.configName2 = Entry(self.compWin)
        self.configName2.grid(row=4, column=0, padx=(10, 10), pady=(4, 4))

        self.configVal2 = Entry(self.compWin)
        self.configVal2.grid(row=4, column=1, padx=(10, 10), pady=(4, 4))

        self.cofigLabel3 = Label(self.compWin, text="Configuration 3 : ")
        self.cofigLabel3.grid(row=5, column=0, padx=(2, 10), pady=(8, 0))
        
        self.valLabel3 = Label(self.compWin, text="Value : ")
        self.valLabel3.grid(row=5, column=1, padx=(10, 10), pady=(8, 0))

        self.configName3 = Entry(self.compWin)
        self.configName3.grid(row=6, column=0, padx=(10, 10), pady=(4, 4))

        self.configVal3 = Entry(self.compWin)
        self.configVal3.grid(row=6, column=1, padx=(10, 10), pady=(4, 4))
        
        
        addcompButton = Button(self.compWin, text="Add Component")
        addcompButton.grid(row=7, column=1, padx=(10, 10), pady=(10, 10), sticky=SE)

       


