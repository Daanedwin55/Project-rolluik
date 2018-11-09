'''
Created on 4 Nov 2018

@author: seanv

Hihi, t was al af xd


'''
import serial
from model import serialSettings as settings
from model import rolluik as sesam

def getUltrasoonArduino(rolluik):
    comport=settings.rolluikDict.get(rolluik)
    serial = serial.Serial(comport= comport, baudrate = settings.baudrate, timeout = settings.timeout)
    serial.write(b'd') #Moet ook licht zijn in C-code
    ultrasoon = serial.read() #of readline().decode('ascii') als er ascii gebruikt is =)
    return ultrasoon

def getUltrasoon(rolluik):
    return settings.ultra[rolluik-1]

def updateUltrasoon(rolluik):
    settings.ultra[rolluik-1] = getUltrasoonArduino(rolluik)