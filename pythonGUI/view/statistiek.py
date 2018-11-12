'''
Created on 5 Nov 2018

@author: seanv
'''
LARGE_FONT = ("Verdana", 12)
MEDIUM_FONT = ("Verdana", 12)

from tkinter import *
from tkinter import ttk

from view import main

from model import serialSettings
class statistiekGUI(Frame):
    '''
        In serialSettings is een array temp
        [0] = rolluik 1
        [1] = rolluik 2
        [2] = rolluik 3
        [3] = rolluik 4
        [4] = rolluik 5
        
        Ik zou voor een bargraph gaan, tenzij er een temp verloop moet worden gemaakt
        Dan zou ik nog 5 arrays maken, en daar gwn telkens de waardes van
        t rolluik in appenden, zodat je van elk rolluik de temp op een tijd hebt
        zeg maar =)
        
        Oh... Don't break it... Cuz I won't fix it =)
    '''
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Statistiek", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        knop1 = ttk.Button(self, text="Terug", command=lambda: controller.show(main.mainGUI))
        knop1.pack() 
        
        self.update()
        
        
    def update(self):
        
        
        self.after(2000, self.update)