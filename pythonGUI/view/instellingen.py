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
        
        sesam.scanCOM()
        
        varDrop1 = StringVar(self)
        varDrop1.set(serialSettings.rolluikDict.get(1))
        
        varDrop2 = StringVar(self)
        varDrop2.set(serialSettings.rolluikDict.get(2))
        
        varDrop3 = StringVar(self)
        varDrop3.set(serialSettings.rolluikDict.get(3))
       
        varDrop4 = StringVar(self)
        varDrop4.set(serialSettings.rolluikDict.get(4))
        
        varDrop5 = StringVar(self)
        varDrop5.set(serialSettings.rolluikDict.get(5))    
 
        default = serialSettings.rolluikDict.get(1)
        
        #print(serialSettings.rolluikDict.values())
        
        rowI = 5
        for rolluik in range(len(serialSettings.rolluikNaam)):
            

            #Rolluik
            eenheid1 = ttk.Button(self, text=serialSettings.rolluikNaam[rolluik])
            eenheid1.grid(column=0, row=rowI, ipady=5, ipadx=15, padx=5, pady=5)
            
    
            
            
            #Save
            #save = ttk.Button(self, text="Opslaan")
            #save.grid(column=2, row=rowI, pady=5, padx=5)            
            
            rowI +=1
        
        
        knop1 = ttk.Button(self, text="Terug", command=lambda: controller.show(main.mainGUI))
        knop1.grid(row=110, column=1) 
        

        def update1():
            serialSettings.rolluikDict[1] = varDrop1.get()
            
        def update2():
            serialSettings.rolluikDict[2] = varDrop2.get()
            
        def update3():
            serialSettings.rolluikDict[3] = varDrop3.get()
            
        def update4():
            serialSettings.rolluikDict[4] = varDrop4.get()
            
        def update5():
            serialSettings.rolluikDict[5] = varDrop5.get()
        
        #Dropdown menu met comporten
        comports = ttk.OptionMenu(self,varDrop1, *serialSettings.rolluikDict.values())
        comports.grid(column=1, row=5, pady=5, padx=5, ipadx=155)
        varDrop1.set(serialSettings.rolluikDict.get(1))
        save1 = ttk.Button(self, text="Opslaan", command=lambda: update1())
        save1.grid(column=2, row=5)
        
        comport1 = ttk.OptionMenu(self,varDrop2, *serialSettings.rolluikDict.values())
        comport1.grid(column=1, row=6, pady=5, padx=5, ipadx=155)
        varDrop2.set(serialSettings.rolluikDict.get(2))
        save2 = ttk.Button(self, text="Opslaan", command=lambda: update2())
        save2.grid(column=2, row=6)
        
        comport2 = ttk.OptionMenu(self,varDrop3, *serialSettings.rolluikDict.values())
        comport2.grid(column=1, row=7, pady=5, padx=5, ipadx=155)
        varDrop3.set(serialSettings.rolluikDict.get(3))
        save3 = ttk.Button(self, text="Opslaan", command=lambda: update3())
        save3.grid(column=2, row=7)
        
        comport3 = ttk.OptionMenu(self,varDrop4, *serialSettings.rolluikDict.values())
        comport3.grid(column=1, row=8, pady=5, padx=5, ipadx=155)
        varDrop4.set(serialSettings.rolluikDict.get(4))
        save4 = ttk.Button(self, text="Opslaan", command=lambda: update4())
        save4.grid(column=2, row=8)
        
        comport4 = ttk.OptionMenu(self,varDrop5, *serialSettings.rolluikDict.values())
        comport4.grid(column=1, row=9, pady=5, padx=5, ipadx=155)
        varDrop5.set(serialSettings.rolluikDict.get(5))
        save5 = ttk.Button(self, text="Opslaan", command=lambda: update5())
        save5.grid(column=2, row=9)
        #print(serialSettings.rolluikPoort)