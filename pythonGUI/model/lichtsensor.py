'''
Created on 4 Nov 2018

@author: seanv
'''

import serial
from model import serialSettings as settings

def getLichtintensiteitArduino(rolluik):
    comport=settings.rolluikDict.get(rolluik)
    serial = serial.Serial(comport= comport, baudrate = settings.baudrate, timeout = settings.timeout)
    serial.write(b'l') #Moet ook licht zijn in C-code
    lichtintensiteit = serial.read() #of readline().decode('ascii') als er ascii gebruikt is =)
    return lichtintensiteit

def getLichtintensiteit(rolluik):
    return settings.licht[rolluik-1]

def updateLichtintensiteit(rolluik):
    settings.licht[rolluik-1] = getLichtintensiteit(rolluik)