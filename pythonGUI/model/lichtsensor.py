'''
Created on 4 Nov 2018

@author: seanv
'''

import serial
from model import serialSettings as settings

serial = serial.Serial(settings.sensorPort, baudrate = settings.baudrate, timeout = settings.timeout)

def getLichtintensiteit():
    serial.write(b'licht') #Moet ook licht zijn in C-code
    lichtintensiteit = serial.readline.decode('ascii')
    return lichtintensiteit