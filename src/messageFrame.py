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
        
        self.LabelText = StringVar()
        self.LabelText.set("Initiate MeXT-SE Tool")
        
        
        #this creates a new label to the GUI       
        self.msgLabel = Label(self.messageFrame_0, textvariable = self.LabelText, bg="#B2BEB5", anchor='nw')
        self.msgLabel.pack(padx=6,pady=6, fill='both') 

    def packFrame(self):
        self.messageFrame_0.pack_propagate(0) 
        self.messageFrame_0.pack(padx=4, pady=4)

    def printMessage(self, msgText):
        # if you want the button to disappear:
        # button.destroy() or button.pack_forget()
        self.LabelText.set(msgText)

