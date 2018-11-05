'''
Created on 4 Nov 2018

@author: seanv
'''
import serial
from model import serialSettings as settings

serial = serial.Serial(settings.sensorPort, baudrate = settings.baudrate, timeout = settings.timeout)

def getTemperatuur():
    serial.write(b'temperatauur') #Moet ook licht zijn in C-code
    temperatuur = serial.readline.decode('ascii')
    return temperatuur