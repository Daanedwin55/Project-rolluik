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

import matplotlib
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import matplotlib.animation as animation
import threading


#Global Variables
f = Figure(figsize=(1.5,1.5),dpi=100)
a = f.add_subplot(111)


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
        label = Label(self, text="Statistiek", font=LARGE_FONT,background="white")
        label.pack()
        
        knop1 = ttk.Button(self, text="Terug", command=lambda: controller.show(main.mainGUI))
        knop1.pack()
                     

        
        threading.Thread(target=self.update).start()

    def update(self):
        
        global f
        global a
        a.clear()
        a.cla()
        a.bar([1,2,3,4,5],[serialSettings.temp[0],serialSettings.temp[1],serialSettings.temp[2],serialSettings.temp[3],serialSettings.temp[4]],color='orange')       
        canvas = FigureCanvasTkAgg(f,self)
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH,expand=True)
        canvas.get_tk_widget().update()
        
           
        self.after(10000,self.update)