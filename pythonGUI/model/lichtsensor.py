'''
Created on 4 Nov 2018

@author: seanv
'''

import serial
from model import serialSettings as settings

serial = serial.Serial(settings.sensorPort, baudrate = settings.baudrate, timeout = settings.timeout)

def getLichtintensiteit(rolluik):
    comport=settings.rolluikPoort[rolluik -1]
    serial = serial.Serial(comport= comport, baudrate = settings.baudrate, timeout = settings.timeout)
    serial.write(b'l') #Moet ook licht zijn in C-code
    lichtintensiteit = serial.readline.decode('ascii')
    return lichtintensiteit