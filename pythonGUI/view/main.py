'''
Created on 4 Nov 2018

@author: seanv
'''

LARGE_FONT = ("Verdana", 12)
MED_FONT = ("Verdana", 10)

from tkinter import *
from tkinter import ttk

from view import instellingen
from view import control
from view import statistiek

from model import serialSettings
class mainGUI(Frame):
    
    def __init__(self, parent, controller):
        
        Frame.__init__(self, parent)
        Frame.config(self, background="white")
        label = Label(self, text="Overzichtpagina", font=LARGE_FONT, background="white")
        label.grid(column=2, row=0, pady=15)
        
        instelling = ttk.Button(self, text="Instellingen", command=lambda: controller.show(instellingen.instellingGUI))
        instelling.grid(column=5, row=0, pady=15)
        
        statistiek = ttk.Button(self, text="Statistiek", command=lambda: controller.show(statistiek.statistiekGUI))
        statistiek.grid(column=1, row=110, pady=15)

        openAlle = ttk.Button(self, text="Open alle", command=lambda: controller.show(instellingen.instellingGUI))
        openAlle.grid(column=4, row=110)

        sluitAlle = ttk.Button(self, text="Sluit alle", command=lambda: controller.show(instellingen.instellingGUI))
        sluitAlle.grid(column=5, row=110)
        
        
        #Rolluik
        rolluik = Label(self, background="white", font=MED_FONT, text="Rolluik naam")
        rolluik.grid(column=0, row=4)
        
        #Status
        statusL = Label(self, background="white", font=MED_FONT, text="Status")
        statusL.grid(column=1, row=4)
        
        #Temp
        tempL = Label(self, background="white", font=MED_FONT, text="Temperatuur")
        tempL.grid(column=2, row=4)
        
        #Lichtintensiteit
        lichtL = Label(self, background="white", font=MED_FONT, text="Lichtintensiteit")
        lichtL.grid(column=3, row=4)
        
        #Knoppen genereren :3
        rowI = 5 #begint bij Row 5 ofzo =)
        for rolluik in range(len(serialSettings.rolluikNaam)):

            #Rolluik
            eenheid = ttk.Button(self, text=serialSettings.rolluikNaam[rolluik])
            eenheid.grid(column=0, row=rowI, ipady=5, ipadx=15, padx=5, pady=5)
            
            #Status
            status = Button(self,bg=serialSettings.status[rolluik])
            status.grid(column=1, row=rowI, ipady=1, ipadx=9, padx=5, pady=5)
            
            #Temperatuur
            temperatuur = Label(self,text="10 Graden", background="white")
            temperatuur.grid(column=2, row=rowI, pady=5, padx=5)
            
            #Lichtintensiteit
            lichtintensiteit = Label(self, text="143 RARE UNITS", background="white")
            lichtintensiteit.grid(column=3, row=rowI, pady=5, padx=5)
            
            #Controle
            omhoog = ttk.Button(self, text=u"\u25B2")
            omhoog.grid(column=4, row=rowI)
            
            omlaag = ttk.Button(self, text=u"\u25BC")
            omlaag.grid(column=5, row=rowI)
            
            #Row increment :3
            rowI = rowI + 1
        
        