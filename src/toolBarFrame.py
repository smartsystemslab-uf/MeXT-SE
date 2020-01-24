#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

from tkinter import *
from functools import partial
import mainWindow


class toolBarFrame():
    def __init__(self, master):
        self.toolbar = Frame(master,bg="grey")
        self.NewButton = Button(self.toolbar,text="New")
        self.NewButton.pack(side=LEFT, padx=2, pady=2)
        self.synthButton = Button(self.toolbar,text="Synthesis")
        self.synthButton.pack(side=LEFT, padx=2, pady=2) 
        self.toolbar.pack(side=TOP, fill=X)

    def bindFunction(self, newFunction, synthFunction):
        self.NewButton.bind("<Button-1>", newFunction)
        self.synthButton.bind("<Button-1>", synthFunction)
        

