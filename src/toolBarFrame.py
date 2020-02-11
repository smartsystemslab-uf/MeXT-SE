#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

from tkinter import *
from functools import partial
import mainWindow, policyScript
import os
from PIL import ImageTk, Image
from tkinter import filedialog

class toolBarFrame():
    def __init__(self, master):
        NewImage = Image.open("../images/newfile.png")
        NewImage = NewImage.resize((25, 25), Image.ANTIALIAS)
        self.NewPhoto = ImageTk.PhotoImage(NewImage)

        synthImage = Image.open("../images/build-tool.png")
        synthImage = synthImage.resize((25, 25), Image.ANTIALIAS)
        self.synthPhoto = ImageTk.PhotoImage(synthImage)

        plusImage = Image.open("../images/plus.png")
        plusImage = plusImage.resize((25, 25), Image.ANTIALIAS)
        self.plusPhoto = ImageTk.PhotoImage(plusImage)

        sheildImage = Image.open("../images/sheild.png")
        sheildImage = sheildImage.resize((25, 25), Image.ANTIALIAS)
        self.sheildPhoto = ImageTk.PhotoImage(sheildImage)

        policyFileImage = Image.open("../images/policy-file.png")
        policyFileImage = policyFileImage.resize((25, 25), Image.ANTIALIAS)
        self.policyFilePhoto = ImageTk.PhotoImage(policyFileImage)

        addPolicyImage = Image.open("../images/add-poilcy.png")
        addPolicyImage = addPolicyImage.resize((25, 25), Image.ANTIALIAS)
        self.addPolicyPhoto = ImageTk.PhotoImage(addPolicyImage)

        ruleGenImage = Image.open("../images/verified.png")
        ruleGenImage = ruleGenImage.resize((25, 25), Image.ANTIALIAS)
        self.ruleGenPhoto = ImageTk.PhotoImage(ruleGenImage)

        self.filename = ""
        self.securityFlag = 0
        self.securityStatus = StringVar()
        self.securityStatus.set("Sheild OFF")

        self.toolbar = Frame(master,bg="grey")
        
        self.NewButton = Button(self.toolbar, image = self.NewPhoto)
        self.NewButton.pack(side=LEFT, padx=2, pady=2)

        self.synthButton = Button(self.toolbar, image = self.synthPhoto)
        self.synthButton.pack(side=LEFT, padx=2, pady=2) 
        
        self.AddIPModule = Button(self.toolbar, image = self.plusPhoto)
        self.AddIPModule.pack(side=LEFT, padx=2, pady=2) 
       
        self.policyFileButton = Button(self.toolbar, image = self.policyFilePhoto, bg="#EFE3D0")
        self.policyFileButton.pack(side=LEFT, padx=2, pady=2)

        self.ruleGenButton = Button(self.toolbar, image = self.ruleGenPhoto)
        self.ruleGenButton.pack(side=LEFT, padx=2, pady=2)

        self.addPolicyButton = Button(self.toolbar, image = self.addPolicyPhoto, bg="#EFCED0")
        self.addPolicyButton.pack(side=LEFT, padx=2, pady=2)

        self.secureButton = Button(self.toolbar, image = self.sheildPhoto)
        self.secureButton.pack(side=LEFT, padx=2, pady=2)
        self.secureLabel = Label(self.toolbar, textvariable=self.securityStatus)
        self.secureLabel.pack(side=LEFT, padx=2, pady=2)

        self.toolbar.pack(side=TOP, fill=X)

    def bindFunction(self, newFunction, synthFunction, AddModuleFunction):
        self.NewButton.bind("<Button-1>", newFunction)
        self.synthButton.bind("<Button-1>", synthFunction) 
        self.AddIPModule.bind("<Button-1>", AddModuleFunction)
        self.secureButton.bind("<Button-1>", self.securityEnable)

        self.policyFileButton.bind("<Button-1>", self.policyFileBrowser)
        self.ruleGenButton.bind("<Button-1>", self.generatePolicyScipt)
        self.addPolicyButton.bind("<Button-1>", self.AddNewPolicy)

    def securityEnable(self, dummyargs=0):
        if self.securityFlag == 0:
            self.securityStatus.set("Sheild  ON")
            self.securityFlag = 1
        else:
            self.securityFlag = 0
            self.securityStatus.set("Sheild OFF")

    def policyFileBrowser(self, dummyargs=0):
        print("Adding policy File")
        try:
            self.filename = filedialog.askopenfilename(initialdir = "../policy-folder/",title = "Select file",filetypes = (("design files","*.te"),("all files","*.*")))

            print("Added Policy file ", self.filename)
        except:
            print("Error: File path not given")

    def generatePolicyScipt(self, dummyargs=0):
        if self.filename == "":
            print("No Policy file was given...")
        else:
            print("Generating Policy Script...")
            print("Policy file :", self.filename)
            policyScript.GenPolicyScript(self.filename)




    def AddNewPolicy(self, dummyargs=0):
        if self.filename == "":
            print("No Policy file was given...")
        else:
            print("Adding New Policy to ", self.filename)




