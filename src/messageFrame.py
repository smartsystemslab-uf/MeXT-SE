#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

from tkinter import *
from functools import partial


class messageFrame():
    def __init__(self, master):

        self.messageFrame_0 = Frame(master, width = master.winfo_screenwidth() * 0.4, height = master.winfo_screenheight() * 0.2 , bg="#B2BEB5")
        self.windowLabel_0 = Label(master, text= "Log Messages", font=("Courier", 14), bg="#B2BEB5", anchor='nw')
        self.windowLabel_0.pack(padx=4, fill='both')

    def packFrame(self):
        self.messageFrame_0.pack(padx=4, pady=4)

    def printMessage(self, msgText):
        # if you want the button to disappear:
        # button.destroy() or button.pack_forget()
        canv = Canvas(self.messageFrame_0, width=98, height=98, bg="#B2BEB5")
        canv.grid(row=0, column=0)

        label = Label(canv, text= msgText, width=94, height=16, bg="#B2BEB5", anchor='nw')
        #this creates a new label to the GUI
        label.pack(padx=6,pady=6, fill='both')
