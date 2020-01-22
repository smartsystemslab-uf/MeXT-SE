#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

from tkinter import *


class mainWindow():
    def __init__(self, master):

        #*** creating menu bar ***
        topMenu_0 = Menu(master)
        master.config(menu=topMenu_0)

        subMenuFile = Menu(topMenu_0)
        topMenu_0.add_cascade(label="File", menu=subMenuFile)
        subMenuFile.add_command(label="New Project", command=self.printMessage)
        subMenuFile.add_command(label="New...", command=self.printMessage)
        subMenuFile.add_separator()
        subMenuFile.add_command(label="Exit", command=self.printMessage)

        subMenuEdit = Menu(topMenu_0)
        topMenu_0.add_cascade(label="File", menu=subMenuEdit)
        subMenuEdit.add_command(label="Undo", command=self.printMessage)
        subMenuEdit.add_command(label="Redo", command=self.printMessage)


        subMenuHelp = Menu(topMenu_0)
        topMenu_0.add_cascade(label="Help", menu=subMenuHelp)
        subMenuHelp.add_command(label="See Tutorial", command=self.printMessage)
        subMenuHelp.add_command(label="About", command=self.printMessage)


    def printMessage(self):
        print("print within Print Message")

