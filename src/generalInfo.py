#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida

from tkinter import *
import tkinter.messagebox



def showMessageBox(WindowTitle, MessageInfo):
    tkinter.messagebox.showinfo(WindowTitle, MessageInfo)



def showAboutMessage():
    tkinter.messagebox.showinfo('Tool Info', 'MeXT-SE 1.0:\nA System-Level Design Tool to Generate Secure MPSoC.\nDeveloper: Md jubaer Hossain Pantho')
