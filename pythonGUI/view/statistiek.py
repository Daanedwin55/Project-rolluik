'''
Created on 5 Nov 2018

@author: seanv
'''
LARGE_FONT = ("Verdana", 12)

from tkinter import *
from tkinter import ttk

from view import main
class statistiekGUI(Frame):
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Statistiek", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        knop1 = ttk.Button(self, text="Terug", command=lambda: controller.show(main.mainGUI))
        knop1.pack() 