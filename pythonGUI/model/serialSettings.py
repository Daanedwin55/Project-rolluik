'''
Created on 4 Nov 2018

@author: seanv
'''
from model import temperatuursensor as temp
from model import lichtsensor as licht
#Sensor settings
sensorPort = 'COM4'
baudrate = 9600
timeout = 1


#Rolluik bediening settings
rolluikPoort = ['COM4', 'COM5', 'COM6', 'COM7', 'COM8']
rolluikNaam = ['Eenheid 1', 'Eenheid 2', 'Puppies <3', 'Eenhied Daddy', 'TeamDaddy']

#Rolluik status
status = ['green', 'green','green','red','green']


#Temperatuur
Temp = [temp.getTemperatuur(1), temp.getTemperatuur(1), temp.getTemperatuur(1), temp.getTemperatuur(1), temp.getTemperatuur(1)]