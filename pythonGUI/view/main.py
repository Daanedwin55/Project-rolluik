'''
Created on 4 Nov 2018

@author: seanv
'''

LARGE_FONT = ("Verdana", 12)
MED_FONT = ("Verdana", 10)

from tkinter import *
from tkinter import ttk

import time

from view import instellingen
from view import control
from view import statistiek

from model import rolluik as sesam

from model import serialSettings
class mainGUI(Frame):
    
    def __init__(self, parent, controller):
        
         #Combined functions
        def combine_funcs(*funcs):
            def combined_func(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return combined_func
        
        def closeAll():
            for rolluik in range(len(serialSettings.rolluikNaam)):
                sesam.sluitRolluik(rolluik)
            status1.config(background=serialSettings.status[0])
            status2.config(background=serialSettings.status[1])   
            status3.config(background=serialSettings.status[2])
            status4.config(background=serialSettings.status[3])
            status5.config(background=serialSettings.status[4])
            
        def openAll():
            for rolluik in range(len(serialSettings.rolluikNaam)):
                sesam.openRolluik(rolluik)
            status1.config(background=serialSettings.status[0])
            status2.config(background=serialSettings.status[1])   
            status3.config(background=serialSettings.status[2])
            status4.config(background=serialSettings.status[3])
            status5.config(background=serialSettings.status[4])
                
        Frame.__init__(self, parent)
        Frame.config(self, background="white")
        label = Label(self, text="Overzichtpagina", font=LARGE_FONT, background="white")
        label.grid(column=2, row=0, pady=15)
        
        instelling = ttk.Button(self, text="Instellingen", command=lambda: controller.show(instellingen.instellingGUI))
        instelling.grid(column=5, row=0, pady=15)
        
        statistiek = ttk.Button(self, text="Statistiek", command=lambda: controller.show(statistiek.statistiekGUI))
        statistiek.grid(column=1, row=110, pady=15)

        openAlle = ttk.Button(self, text="Open alle", command=lambda: openAll())
        openAlle.grid(column=4, row=110)

        sluitAlle = ttk.Button(self, text="Sluit alle", command=lambda: closeAll())
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
        rowI = 5
        for rolluik in range(len(serialSettings.rolluikNaam)):
            

            #Rolluik
            eenheid1 = ttk.Button(self, text=serialSettings.rolluikNaam[rolluik])
            eenheid1.grid(column=0, row=rowI, ipady=5, ipadx=15, padx=5, pady=5)
            
    
            
            #Temperatuur
            temperatuur1 = Label(self,text="10 Graden", background="white")
            temperatuur1.grid(column=2, row=rowI, pady=5, padx=5)
            
            #Lichtintensiteit
            lichtintensiteit1 = Label(self, text="143 RARE UNITS", background="white")
            lichtintensiteit1.grid(column=3, row=rowI, pady=5, padx=5)            
            
            rowI +=1
        
        #Status
        status1 = Button(self,bg=serialSettings.status[0])
        status1.grid(column=1, row=5, ipady=1, ipadx=9, padx=5, pady=5)
        
        status2 = Button(self,bg=serialSettings.status[1])
        status2.grid(column=1, row=6, ipady=1, ipadx=9, padx=5, pady=5)
        
        status3 = Button(self,bg=serialSettings.status[2])
        status3.grid(column=1, row=7, ipady=1, ipadx=9, padx=5, pady=5)
        
        status4 = Button(self,bg=serialSettings.status[3])
        status4.grid(column=1, row=8, ipady=1, ipadx=9, padx=5, pady=5)
        
        status5 = Button(self,bg=serialSettings.status[4])
        status5.grid(column=1, row=9, ipady=1, ipadx=9, padx=5, pady=5)
        
        #Controle
        omhoog1 = ttk.Button(self, text=u"\u25B2", command=lambda : combine_funcs(sesam.openRolluik(0), status1.config(background=serialSettings.status[0])))
        omhoog1.grid(column=4, row=5)
            
        omlaag1 = ttk.Button(self, text=u"\u25BC", command=lambda : combine_funcs(sesam.sluitRolluik(0), status1.config(background=serialSettings.status[0])))
        omlaag1.grid(column=5, row=5)
        
        omhoog2 = ttk.Button(self, text=u"\u25B2", command=lambda : combine_funcs(sesam.openRolluik(1), status2.config(background=serialSettings.status[1])))
        omhoog2.grid(column=4, row=6)
            
        omlaag2 = ttk.Button(self, text=u"\u25BC", command=lambda : combine_funcs(sesam.sluitRolluik(1), status2.config(background=serialSettings.status[1])))
        omlaag2.grid(column=5, row=6)
    
        omhoog3 = ttk.Button(self, text=u"\u25B2", command=lambda : combine_funcs(sesam.openRolluik(2), status3.config(background=serialSettings.status[2])))
        omhoog3.grid(column=4, row=7)
            
        omlaag3 = ttk.Button(self, text=u"\u25BC", command=lambda : combine_funcs(sesam.sluitRolluik(2), status3.config(background=serialSettings.status[2])))
        omlaag3.grid(column=5, row=7)
        
        omhoog4 = ttk.Button(self, text=u"\u25B2", command=lambda : combine_funcs(sesam.openRolluik(3), status4.config(background=serialSettings.status[3])))
        omhoog4.grid(column=4, row=8)
            
        omlaag4 = ttk.Button(self, text=u"\u25BC", command=lambda : combine_funcs(sesam.sluitRolluik(3), status4.config(background=serialSettings.status[3])))
        omlaag4.grid(column=5, row=8)
        
        omhoog5 = ttk.Button(self, text=u"\u25B2", command=lambda : combine_funcs(sesam.openRolluik(4), status5.config(background=serialSettings.status[4])))
        omhoog5.grid(column=4, row=9)
            
        omlaag5 = ttk.Button(self, text=u"\u25BC", command=lambda : combine_funcs(sesam.sluitRolluik(4), status5.config(background=serialSettings.status[4])))
        omlaag5.grid(column=5, row=9)
        


        
        