'''
Created on 4 Nov 2018

@author: seanv
'''
import serial
from model import serialSettings as settings
from model import rolluik as sesam

def getUltrasoonArduino(rolluik):
    comport=settings.rolluikDict.get(rolluik)
    daddy = serial.Serial(port= comport, baudrate = settings.baudrate, timeout = settings.timeout)
    daddy.write(b'd') #Moet ook licht zijn in C-code
    ultrasoon = daddy.read() #of readline().decode('ascii') als er ascii gebruikt is =)
    return ultrasoon

def getUltrasoon(rolluik):
    return settings.ultra[rolluik-1]

def updateUltrasoon(rolluik):
    settings.ultra[rolluik-1] = getUltrasoonArduino(rolluik)