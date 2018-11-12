'''
Created on 4 Nov 2018

@author: seanv
'''
from model import temperatuursensor as temp
from model import lichtsensor as licht
#Sensor settings
sensorPort = ['COM4']
baudrate = 19200
timeout = 1


#Rolluik bediening settings
rolluikPoort = ['COM4', 'COM5', 'COM6', 'COM7', 'COM8']
rolluikNaam = ['Eenheid 1', 'Eenheid 2', 'Puppies <3', 'Eenhied Daddy', 'TeamDaddy']
rolluikDict = {1:'COM4',2:'COM5',3:'COM6',4:'COM7',5:'COM8'}

#Rolluik status
status = ['black', 'black','black','black','black']


#Temperatuur
#!!! REF BEFORE ASSIGNMENT ERROR !!! Temp = [temp.getTemperatuur(1), temp.getTemperatuur(1), temp.getTemperatuur(1), temp.getTemperatuur(1), temp.getTemperatuur(1)]
temp = [21.2,20.8,22.2,21.9,22.1]
maxTemp = 25 #Temperatuur waarbij de rolluik omlaag gaan met de functie temperatuurSensor.setTemperatuur(rolluik, int(temperatuur)) :3

#Lichtintensiteit
licht = [90,90,80,80,70]
maxLicht = 1400 #LUX

#Ultrasoon
ultra = [2,2,2,2,2]