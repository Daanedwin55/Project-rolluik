'''
Created on 4 Nov 2018

@author: seanv
'''
import serial
from model import serialSettings as settings

# Status opvragen enzo

def getStatus(rolluiknummer):
    comport = settings.rolluikPoort[rolluiknummer -1] #-1 omdat eenheid 1 is index 0
    serial = serial.Serial(comport=comport, baudrate = settings.baudrate, timeout = settings.timeout)
    serial.Write(b'hihi') #moet ook 'hihi' zijn in C om rolluik status op te vragen
    status = serial.readline.decode('ascii')
    if status == 1:
        return 'open' 
    else:
        return 'dicht'

# Open / sluit shizle
def sluitAlle():
    for comport in settings.rolluikPoort:
        serial = serial.Serial(comport = comport, baudrate = settings.baudrate, timeout = settings.timeout)
        serial.write(b'sluit') #moet ook 'sluit' zijn in C om rolluik te sluiten

def openAlle():
    for comport in settings.rolluikPoort:
        serial = serial.Serial(comport = comport, baudrate = settings.baudrate, timeout = settings.timeout)
        serial.write(b'open') #moet ook 'open' zijn in C om rolluik te openen

def sluitRolluik(rolluiknummer):
    comport = settings.rolluikPoort[rolluiknummer -1] #-1 omdat eenheid 1 is index 0
    serial = serial.Serial(comport=comport, baudrate = settings.baudrate, timeout = settings.timeout)
    serial.Write(b'sluit') #moet ook 'sluit' zijn in C om rolluik te sluiten

def openRolluik(rolluiknummer):
    comport = settings.rolluikPoort[rolluiknummer -1] #-1 omdat eenheid 1 is index 0
    serial = serial.Serial(comport=comport, baudrate = settings.baudrate, timeout = settings.timeout)
    serial.Write(b'open') #moet ook 'open' zijn in C om rolluik te openen