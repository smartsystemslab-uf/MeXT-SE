#MeXT-SE software source code
#author: Md Jubaer Hossain Pantho
#University of Florida


from tkinter import *
from tkinter.ttk import *

import sys, os
import mainWindow






root = Tk()

mainWindowObj = mainWindow.mainWindow(root)
root.title('MeXT-SE')
root.wm_iconbitmap(bitmap = "@../images/mext-se.xbm")
root.resizable(width=False, height=False)
#program_directory=sys.path[0]
#root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "mext-se.png")))


root.mainloop()
