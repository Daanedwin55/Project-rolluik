'''
Created on 4 Nov 2018

@author: seanv
'''
import serial
from model import serialSettings as settings
from model import rolluik as sesam


from random import randint
def calcTemp(temp):
    return (temp * (140/255)) -40

def liveTest():
    i = randint(20,30)
    settings.temp[0] = i

def getTemperatuurArduino(rolluik):
    comport=settings.rolluikDict.get(rolluik)
    daddy = serial.Serial(port= comport, baudrate = settings.baudrate, timeout = settings.timeout)
    daddy.write(b't') #Moet ook licht zijn in C-code
    raw_temperatuur = daddy.read() #of readline().decode('ascii') als er ascii gebruikt is =)
    temperatuur = calcTemp(raw_temperatuur)
    return temperatuur

def getTemperatuur(rolluik):
    return settings.temp[rolluik-1]

def updateTemperatuur(rolluik):
    settings.temp[rolluik-1] = getTemperatuurArduino(rolluik)
    
def setTemperatuur(rolluik, temperatuur):
    settings.temp[rolluik-1] = temperatuur
    if(int(temperatuur) > settings.maxTemp):
        sesam.sluitRolluik(int(rolluik))
    else:
        sesam.openRolluik(int(rolluik))
