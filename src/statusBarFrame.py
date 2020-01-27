#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

from tkinter import *
from functools import partial

class statusBarFrame():
    def __init__(self, master):

        self.statusBar = Label(master, text="Preparing to show status...", bd=1, relief=SUNKEN, anchor=W)
        self.statusBar.pack(side=BOTTOM, fill=X)

