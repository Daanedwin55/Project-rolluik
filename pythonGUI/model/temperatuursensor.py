'''
Created on 4 Nov 2018

@author: seanv
'''
import serial
from model import serialSettings as settings



def getTemperatuur(rolluik):
    comport=settings.rolluikPoort[rolluik -1]
    serial = serial.Serial(comport= comport, baudrate = settings.baudrate, timeout = settings.timeout)
    serial.write(b't') #Moet ook licht zijn in C-code
    temperatuur = serial.readline.decode('ascii')
    return temperatuur