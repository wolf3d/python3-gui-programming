# Hello, World application for Tkinter

"""
This isn't best practice, because it fills your namespace with a lot of 
classes, which you might accidentally overwrite, but it's okay for very
small scripts.
"""
from tkinter import *
from tkinter.ttk import *

root = Tk()
label = Label(root, text="Hello, World")
label.pack()
root.mainloop()