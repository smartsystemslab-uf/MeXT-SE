#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida


from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

import sys, os
import mainWindow






root = Tk()

mainWindowObj = mainWindow.mainWindow(root)
root.title('MeXT-SE')
root.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(file='../images/mext-se.png'))


root.mainloop()
