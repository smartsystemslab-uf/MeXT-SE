#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

from tkinter import *
from functools import partial

class mainWindow():
    def __init__(self, master):

        #########################################
        #*** creating menu bar ***
        #########################################
        topMenu_0 = Menu(master)
        master.config(menu=topMenu_0)
        master.minsize(width=640, height=480)

        #########################################
        # ***** Main Window for source code *****
        #########################################


        sourceFrame_0 = Frame(master, width = master.winfo_screenwidth() * 0.4, height = master.winfo_screenheight() * 0.4, bg="#B3B3D3")
        messageFrame_0 = Frame(master, width = master.winfo_screenwidth() * 0.4, height = master.winfo_screenheight() * 0.2 , bg="#B2BEB5")
       

        #########################################

        #Creating File sub menu ***
        subMenuFile = Menu(topMenu_0)
        topMenu_0.add_cascade(label = "File", menu=subMenuFile)
        subMenuFile.add_command(label = "New Project", command=self.NewProjectFunc)
        subMenuFile.add_command(label = "New...", command=self.NewFunc)
        subMenuFile.add_separator()

        ExitFunction = partial(self.ExitFunc, master, messageFrame_0)
        subMenuFile.add_command(label = "Exit", command = ExitFunction)

        #Creating Edit sub menu *** 
        subMenuEdit = Menu(topMenu_0)
        topMenu_0.add_cascade(label = "Edit", menu=subMenuEdit)
        subMenuEdit.add_command(label = "Undo", command=self.UndoFunc)
        subMenuEdit.add_command(label = "Redo", command=self.RedoFunc)


        #Creating Tool sub menu *** 
        subMenuTool = Menu(topMenu_0)
        topMenu_0.add_cascade(label="Tool", menu=subMenuTool)
        RunSynthesisFunction = partial(self.RunSynthesis, messageFrame_0)
        subMenuTool.add_command(label="Run Synthesis", command=RunSynthesisFunction)
        subMenuTool.add_command(label="Customize...", command=self.Customize)

        #Creating Help sub menu *** 
        subMenuHelp = Menu(topMenu_0)
        topMenu_0.add_cascade(label="Help", menu=subMenuHelp)
        subMenuHelp.add_command(label="See Tutorial", command=self.seeTutorialFunc)
        subMenuHelp.add_command(label="About", command=self.AboutFunc)


        #########################################
        # ***** Toolbar *****
        #########################################

        toolbar = Frame(master,bg="grey")
        NewButton = Button(toolbar,text="New", command = self.NewFunc)
        NewButton.pack(side=LEFT, padx=2, pady=2)
        synthButton = Button(toolbar,text="Synthesis", command = RunSynthesisFunction)
        synthButton.pack(side=LEFT, padx=2, pady=2) 
        toolbar.pack(side=TOP, fill=X)



        sourceFrame_0.pack(padx=4, pady=4)
        messageFrame_0.pack(padx=4, pady=4)


#File methods

    def NewProjectFunc(self):
        print("running NewProjectFunc")

    def NewFunc(self):
        print("running NewFunc")

    def ExitFunc(self, master, messageFrame_0):
        self.printMessage(messageFrame_0, "Exiting")
        print("Exiting...")
        #master.destroy()




#Edit methods

    def UndoFunc(self):
        print("running UndoFunc")

    def RedoFunc(self):
        print("running RedoFunc")


#Tool methods

    def RunSynthesis(self, messageFrame_0):
        self.printMessage(messageFrame_0, "Run Synthesis")
        print("Generating TCL script...")

    def Customize(self):
        print("running Customize")

#Help methods

    def seeTutorialFunc(self):
        print("running seeTutorialFunc")

    def AboutFunc(self):
        print("running AboutFunc")

    def printMessage(self, messageFrame_0, msgText):
        # if you want the button to disappear:
        # button.destroy() or button.pack_forget()
        canv = Canvas(messageFrame_0, width=98, height=98, bg="#B2BEB5")
        canv.grid(row=0, column=0)
        label = Label(canv, text= msgText, width=94, height=16, bg="#B2BEB5", anchor='nw')
        #this creates a new label to the GUI
        label.pack(padx=6,pady=6, fill='both')




