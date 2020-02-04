from tkinter import *
from tkinter.ttk import *
import xml.dom.minidom
import IPparse
from PIL import ImageTk, Image


class DesignTree():
    def __init__(self, master):
    
        self.tree = Treeview(master, height=30)
        Style().configure("Treeview", background="#B3B3D0", font=(None, 12), foreground="black", fieldbackground="#B3B3D0")

        self.tree["columns"]=("one","two")
        self.tree.column("#0", width=280, minwidth=240, stretch=NO)
        self.tree.column("one", width=120, minwidth=100, stretch=NO)
        self.tree.column("two", width=160, minwidth=120)

        self.tree.heading("#0",text="Design Tree",anchor=W)
        self.tree.heading("one", text="--",anchor=W)
        self.tree.heading("two", text="info",anchor=W)

        greenImage = Image.open("../images/greenButton.png")
        greenImage = greenImage.resize((15, 15), Image.ANTIALIAS)
        self.greenPhoto = ImageTk.PhotoImage(greenImage)

    def generateTree(self, filePath):

        systemData, cpuConfList, memConfList, comConfData = IPparse.parseFile(filePath)

        # Level 1
        self.treeInfo= []
        vendorInfo = self.tree.insert("", 1, text=str(systemData[0][0]), values=("","vendor Info"))
        boardInfo = self.tree.insert("", 2, text=str(systemData[1][0]),values=("","board Info"))

        self.treeInfo.append(vendorInfo)
        self.treeInfo.append(boardInfo)


        for i in range(2, len(systemData)):
            moduleBuffer = self.tree.insert("",i, text=str(systemData[i][0]), image = self.greenPhoto, values=("",""))
            self.treeInfo.append(moduleBuffer)


        # Level 2


        for i in range(2, len(systemData)):

            #Adding CPU configuration information
            if "CPU" in str(systemData[i][0]) and cpuConfList:
                cpuConfig = self.tree.insert(self.treeInfo[i], "end", text="cpuconfig", values=("","customize"))

                for j in range(len(cpuConfList)):
                    self.tree.insert(cpuConfig, "end", text=cpuConfList[j], values=("",""))
            #Adding Memory Configuration information
            elif "memory" in str(systemData[i][0]) and memConfList:
                memConfig = self.tree.insert(self.treeInfo[i], "end", text="memconfig", values=("","customize"))
                for j in range(len(memConfList)):
                    self.tree.insert(memConfig, "end", text=memConfList[j], values=("",""))


            for k in range(1, len(systemData[i])):
                self.tree.insert(self.treeInfo[i], "end", text=systemData[i][k], values=("",""))


        #Adding Communication configuration
        if comConfData:
            moduleBuffer = self.tree.insert("","end", text=comConfData, image = self.greenPhoto, values=("","BUS"))
            self.treeInfo.append(moduleBuffer)
        self.tree.grid(column = 0, row = 3, padx=(8, 8))
