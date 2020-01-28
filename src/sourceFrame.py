#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

from tkinter import *
from functools import partial
import os
import messageFrame, toolBarFrame, statusBarFrame
import generalInfo
import os

class sourceFrame():
    def __init__(self, master):

        self.fileList = os.listdir("../")

        self.sourceFrame_0 = Frame(master, width = master.winfo_screenwidth() * 0.4, height = master.winfo_screenheight() * 0.4, bg="#B3B3D3")
        self.sourceFrame_0.pack_propagate(0)
        self.sourceFrame_0.pack(padx=4, pady=4)


        self.LeftFrame = Canvas(self.sourceFrame_0, width=master.winfo_screenwidth() * 0.1, height=master.winfo_screenheight() * 0.4, bg="#C2BEB0")
        self.LeftFrame.grid(row=0, column=0)
        self.LeftFrame.pack_propagate(0) 
        self.LeftLabel_0 = Label(self.LeftFrame, text= "Directory", font=("Courier", 14), bg="#C2BEB0", anchor='nw')
        self.LeftLabel_0.pack(padx=4, pady=4)


        self.RightFrame = Canvas(self.sourceFrame_0, width=master.winfo_screenwidth() * 0.3, height=master.winfo_screenheight() * 0.4, bg="#B3B3D3")
        self.RightFrame.grid(row=0, column=1)
        self.RightFrame.pack_propagate(0)


        self.listBox = Listbox(self.LeftFrame, height=27, bg="#C2BEB0")
        self.listBox.pack(padx=4, pady=4, fill='both')
        
        for item in self.fileList:
            self.listBox.insert(END, item)
