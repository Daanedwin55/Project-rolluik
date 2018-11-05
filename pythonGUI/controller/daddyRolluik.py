'''
Created on 4 Nov 2018

@author: seanv

Controller die bestuurd welke frames op het scherm getoond worden :)

TODO:

    Pagina voor:
        - Control
        - Instellingen
        - Statistiek
        maken
        
    Daadwerkelijk data uit seriele communicatie gaan gebruiken om objecten te modificeren =)
    
    Thats about it... :)
        
'''
from tkinter import *

from view import main

from view import control

from view import instellingen

from view import statistiek

class root(Tk):
    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        
        Tk.title(self, "Team Daddy - Rolluiksysteem")
        Tk.maxsize(self, 610, 350)
        Tk.minsize(self, 610, 350)
        Tk.config(self, background="white")
        
        scherm = Frame(self)
        scherm.grid(row=0, column=2, sticky="nsew")
        scherm.grid_rowconfigure(0, weight=1)
        scherm.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
                
        for F in (main.mainGUI, control.controlGUI, instellingen.instellingGUI, statistiek.statistiekGUI):
            
            frame = F(scherm, self)
            
            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show(main.mainGUI)

        
    def show(self, scherm):
        
        frame = self.frames[scherm]
        frame.tkraise()
        
app = root()
app.mainloop()