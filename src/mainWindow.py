#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

from tkinter import *
from functools import partial
import sourceFrame, messageFrame, toolBarFrame, statusBarFrame
import generalInfo
import os
import logicEngine

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
        subMenuFile.add_command(label = "New Project      ", command=self.NewProjectFunc)
        subMenuFile.add_command(label = "New...", command=self.NewFunc)
        subMenuFile.add_separator()

        ExitFunction = partial(self.ExitFunc, master)
        subMenuFile.add_command(label = "Exit", command = ExitFunction)

        #Creating Edit sub menu *** 
        subMenuEdit = Menu(topMenu_0)
        topMenu_0.add_cascade(label = "Edit", menu=subMenuEdit)
        subMenuEdit.add_command(label = "Undo      ", command=self.UndoFunc)
        subMenuEdit.add_command(label = "Redo   ", command=self.RedoFunc)


        #Creating Tool sub menu *** 
        subMenuTool = Menu(topMenu_0)
        topMenu_0.add_cascade(label="Tool", menu=subMenuTool)
        subMenuTool.add_command(label="Run Synthesis", command=self.RunSynthesis)

        subMenuTool.add_separator()
        subMenuTool.add_command(label="Add Policy File...", command=self.AddFilePolcy)
        subMenuTool.add_command(label="Add New Rule...", command=self.AddNewRule)
        subMenuTool.add_command(label="Generate Policy Script...  ", command=self.GenPolicyScript)


        #Creating Help sub menu *** 
        subMenuHelp = Menu(topMenu_0)
        topMenu_0.add_cascade(label="Help", menu=subMenuHelp)
        subMenuHelp.add_command(label="See Tutorial      ", command=self.seeTutorialFunc)
        subMenuHelp.add_command(label="About", command=self.AboutFunc)


        #########################################
        # ***** Toolbar *****
        #########################################

        self.toolBarInterface = toolBarFrame.toolBarFrame(master)
        self.toolBarInterface.bindFunction(self.NewFunc, self.RunSynthesis, self.AddModule)


        #########################################
        # ***** Main Window for source code *****
        #########################################
        self.sourceFrame_0 = sourceFrame.sourceFrame(master)

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
        try:
            self.sourceFrame_0.treeData.deletePrevousEntry()
        except:    
            self.messageFrameInterface.printMessage("Error: Unknown type...")

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
        try:
            logicEngine.assembleTree(self.sourceFrame_0.filename)
        except:
            self.messageFrameInterface.printMessage("XML file not found ...")
            print("Error: XML file not found ...")


    def AddModule(self, dummyargs=0):
        self.messageFrameInterface.printMessage("Adding Module ...")
        print("Adding new Module ...")
        

        

    def AddFilePolcy(self):
        print("Adding Policy File...")
        self.messageFrameInterface.printMessage("Adding Policy File...")
        self.toolBarInterface.policyFileBrowser()

    def AddNewRule(self):
        print("Adding New Rule...")
        self.messageFrameInterface.printMessage("Adding New Rule...")

    def GenPolicyScript(self):
        print("Generate Policy Script...")
        self.messageFrameInterface.printMessage("Generate Policy Script...")
        self.toolBarInterface.generatePolicyScipt()

#Help methods

    def seeTutorialFunc(self):
        print("running seeTutorialFunc")
        self.messageFrameInterface.printMessage("MeXT-SE tutorial link ...")

    def AboutFunc(self):
        print("running AboutFunc")
        self.messageFrameInterface.printMessage("About MeXT-SE ...")
        generalInfo.showAboutMessage()




