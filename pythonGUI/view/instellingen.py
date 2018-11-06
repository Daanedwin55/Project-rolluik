'''
Created on 4 Nov 2018

@author: seanv
'''

LARGE_FONT = ("Verdana", 12)

import serial.tools.list_ports as list_ports
from tkinter import *
from tkinter import ttk

from view import control
from view import main

from model import rolluik as sesam

from model import serialSettings
class instellingGUI(Frame):
    
    def __init__(self, parent, controller):
        
        
        Frame.__init__(self, parent)
        Frame.config(self, background="white")
        label = Label(self, text="Instellingen", font=LARGE_FONT, background="white")
        label.grid(row=0, column=1,pady=15)
        
        
        varDrop1 = StringVar(self)
        varDrop2 = StringVar(self)
        varDrop3 = StringVar(self)
        varDrop4 = StringVar(self)
        varDrop5 = StringVar(self)
        rowI = 5
        for rolluik in range(len(serialSettings.rolluikNaam)):
            

            #Rolluik
            eenheid1 = ttk.Button(self, text=serialSettings.rolluikNaam[rolluik])
            eenheid1.grid(column=0, row=rowI, ipady=5, ipadx=15, padx=5, pady=5)
            
    
            
            
            #Save
            save = ttk.Button(self, text="Opslaan")
            save.grid(column=2, row=rowI, pady=5, padx=5)            
            
            rowI +=1
        
        
        knop1 = ttk.Button(self, text="Terug", command=lambda: controller.show(main.mainGUI))
        knop1.grid(row=110, column=1) 
        
        #Dropdown menu met comporten
        comports = ttk.OptionMenu(self,varDrop1, *serialSettings.rolluikPoort)
        comports.grid(column=1, row=5, pady=5, padx=5, ipadx=155)
        
        comport1 = ttk.OptionMenu(self,varDrop2, *serialSettings.rolluikPoort)
        comport1.grid(column=1, row=6, pady=5, padx=5, ipadx=155)
        
        comport2 = ttk.OptionMenu(self,varDrop3, *serialSettings.rolluikPoort)
        comport2.grid(column=1, row=7, pady=5, padx=5, ipadx=155)
        
        comport3 = ttk.OptionMenu(self,varDrop4, *serialSettings.rolluikPoort)
        comport3.grid(column=1, row=8, pady=5, padx=5, ipadx=155)
        
        comport4 = ttk.OptionMenu(self,varDrop5, *serialSettings.rolluikPoort)
        comport4.grid(column=1, row=9, pady=5, padx=5, ipadx=155)
        
        print(serialSettings.rolluikPoort)