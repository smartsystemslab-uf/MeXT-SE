#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

from tkinter import *
from functools import partial
import messageFrame, toolBarFrame, statusBarFrame
import generalInfo
import os

class mainWindow():
    def __init__(self, master):

        #########################################
        #*** creating menu bar ***
        #########################################
        topMenu_0 = Menu(master)
        master.config(menu=topMenu_0)
        master.minsize(width=640, height=480)



        #Creating File sub menu ***
        subMenuFile = Menu(topMenu_0)
        topMenu_0.add_cascade(label = "File", menu=subMenuFile)
        subMenuFile.add_command(label = "New Project", command=self.NewProjectFunc)
        subMenuFile.add_command(label = "New...", command=self.NewFunc)
        subMenuFile.add_separator()

        ExitFunction = partial(self.ExitFunc, master)
        subMenuFile.add_command(label = "Exit", command = ExitFunction)

        #Creating Edit sub menu *** 
        subMenuEdit = Menu(topMenu_0)
        topMenu_0.add_cascade(label = "Edit", menu=subMenuEdit)
        subMenuEdit.add_command(label = "Undo", command=self.UndoFunc)
        subMenuEdit.add_command(label = "Redo", command=self.RedoFunc)


        #Creating Tool sub menu *** 
        subMenuTool = Menu(topMenu_0)
        topMenu_0.add_cascade(label="Tool", menu=subMenuTool)
        subMenuTool.add_command(label="Run Synthesis", command=self.RunSynthesis)
        subMenuTool.add_command(label="Customize...", command=self.Customize)

        #Creating Help sub menu *** 
        subMenuHelp = Menu(topMenu_0)
        topMenu_0.add_cascade(label="Help", menu=subMenuHelp)
        subMenuHelp.add_command(label="See Tutorial", command=self.seeTutorialFunc)
        subMenuHelp.add_command(label="About", command=self.AboutFunc)


        #########################################
        # ***** Toolbar *****
        #########################################

        self.toolBarInterface = toolBarFrame.toolBarFrame(master)
        self.toolBarInterface.bindFunction(self.NewFunc, self.RunSynthesis, self.AddModule)

        self.fileList = os.listdir()


        #self.fileListFrame_0.pack(side=LEFT, padx=4, pady=4)

        #########################################
        # ***** Main Window for source code *****
        #########################################
        self.sourceFrame_0 = Frame(master, width = master.winfo_screenwidth() * 0.4, height = master.winfo_screenheight() * 0.4, bg="#B3B3D3")
        self.sourceFrame_0.pack_propagate(0)
        self.sourceFrame_0.pack(padx=4, pady=4)

        self.LeftFrame = Canvas(self.sourceFrame_0, width=master.winfo_screenwidth() * 0.1, height=master.winfo_screenheight() * 0.4, bg="#C2BEB0")
        self.LeftFrame.grid(row=0, column=0)
        self.LeftFrame.pack_propagate(0)
        self.RightFrame = Canvas(self.sourceFrame_0, width=master.winfo_screenwidth() * 0.3, height=master.winfo_screenheight() * 0.4, bg="#B3B3D3")
        self.RightFrame.grid(row=0, column=1)
        self.RightFrame.pack_propagate(0)


        self.listBox = Listbox(self.LeftFrame, height=27, bg="#C2BEB0")
        self.listBox.pack(fill='both')
        
        for item in self.fileList:
            self.listBox.insert(END, item)

        #########################################
        # *** Main Window for showing message ***
        #########################################
        self.messageFrameInterface = messageFrame.messageFrame(master)
        self.messageFrameInterface.packFrame()

        #########################################
        # ***            Status Bar           ***
        #########################################
        self.statusInfo = statusBarFrame.statusBarFrame(master)
        


#File methods

    def NewProjectFunc(self):
        print("running NewProjectFunc")
        self.messageFrameInterface.printMessage("Creating New Project...")


    def NewFunc(self, dummyargs=0):
        print("running NewFunc")
        self.messageFrameInterface.printMessage("Creating New file ...")

    def ExitFunc(self, master):
        self.messageFrameInterface.printMessage("Exiting ...")
        print("Exiting ...")
        master.destroy()




#Edit methods

    def UndoFunc(self):
        print("running UndoFunc")

    def RedoFunc(self):
        print("running RedoFunc")


#Tool methods

    def RunSynthesis(self, dummyargs=0):
        self.messageFrameInterface.printMessage("Generating TCL script ...")
        print("Generating TCL script ...")


    def AddModule(self, dummyargs=0):
        self.messageFrameInterface.printMessage("Adding Module ...")
        print("Adding new Module ...")
        

        

    def Customize(self):
        print("running Customize")
        self.messageFrameInterface.printMessage("Customizing ...")

#Help methods

    def seeTutorialFunc(self):
        print("running seeTutorialFunc")
        self.messageFrameInterface.printMessage("MeXT-SE tutorial link ...")

    def AboutFunc(self):
        print("running AboutFunc")
        self.messageFrameInterface.printMessage("About MeXT-SE ...")
        generalInfo.showAboutMessage()




